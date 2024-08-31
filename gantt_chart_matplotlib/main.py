import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

pd.set_option('display.max_columns', None)

df = pd.DataFrame({'task': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
                   'team': ['R&D', 'Accounting', 'Sales', 'Sales', 'IT', 'R&D', 'IT', 'Sales', 'Accounting',
                            'Accounting', 'Sales', 'IT'],
                   'start': pd.to_datetime(
                       ['20 Oct 2022', '24 Oct 2022', '26 Oct 2022', '31 Oct 2022', '3 Nov 2022', '7 Nov 2022',
                        '10 Nov 2022', '14 Nov 2022', '18 Nov 2022', '23 Nov 2022', '28 Nov 2022', '30 Nov 2022']),
                   'end': pd.to_datetime(
                       ['31 Oct 2022', '28 Oct 2022', '31 Oct 2022', '8 Nov 2022', '9 Nov 2022', '18 Nov 2022',
                        '17 Nov 2022', '22 Nov 2022', '23 Nov 2022', '1 Dec 2022', '5 Dec 2022', '5 Dec 2022']),
                   'completion_frac': [1, 1, 1, 1, 1, 0.95, 0.7, 0.35, 0.1, 0, 0, 0]})

# 1. How many days passed/would pass from the overall project start to the start date of each task
df['days_to_start'] = (df['start'] - df['start'].min()).dt.days

# 2. How many days passed/would pass from the overall project start to the end date of each task
df['days_to_end'] = (df['end'] - df['start'].min()).dt.days

# 3. The duration of each task, including both the start and end dates:
df['task_duration'] = df['days_to_end'] - df['days_to_start'] + 1  # to include also the end date

# 4. The status of completion of each task translated from a fraction into a portion of days allocated to that task
df['completion_days'] = df['completion_frac'] * df['task_duration']

plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.show()

# two or more subtasks spread out over a period of time, use broken_barh()
# 1. Those tasks assigned to the Sales team
df_sales_subtask = df[df['team'] == 'Sales'][['task', 'team', 'start', 'end']]

# 2. Rename the columns start and end to start_1 and end_1
df_sales_subtask.rename(columns={'start': 'start_subtask_1', 'end': 'end_subtask_1'}, inplace=True)
df_sales_subtask.reset_index(drop=True, inplace=True)

# 3. Add more subtasks to some of the available tasks
df_sales_subtask['start_subtask_2'] = pd.to_datetime([None, '10 Nov 2022', '25 Nov 2022', None])
df_sales_subtask['end_subtask_2'] = pd.to_datetime([None, '14 Nov 2022', '28 Nov 2022', None])
df_sales_subtask['start_subtask_3'] = pd.to_datetime([None, None, '1 Dec 2022', None])
df_sales_subtask['end_subtask_3'] = pd.to_datetime([None, None, '5 Dec 2022', None])

print(df_sales_subtask)

# 4.
for i in [1, 2, 3]:
    suffix = '_' + str(i)
    df_sales_subtask['days_to_start' + suffix] = (
                df_sales_subtask['start_subtask' + suffix] - df_sales_subtask['start_subtask_1'].min()).dt.days
    df_sales_subtask['days_to_end' + suffix] = (
                df_sales_subtask['end_subtask' + suffix] - df_sales_subtask['start_subtask_1'].min()).dt.days
    df_sales_subtask['task_duration' + suffix] = df_sales_subtask['days_to_end' + suffix] - df_sales_subtask[
        'days_to_start' + suffix] + 1

fig, ax = plt.subplots()

# 2. Iterate through the rows of the dataframe and check if the task has one, two, or three subtasks. Based on that,
# do the following: One subtask: plot a bar using the barh() method as we did earlier. Two subtasks: plot two bars
# using the broken_barh() method. Three subtasks: plot three bars using the broken_barh() method
for index, row in df_sales_subtask.iterrows():
    if row['start_subtask_2'] is None:
        ax.barh(y=df_sales_subtask['task'], width=df_sales_subtask['task_duration_1'],
                left=df_sales_subtask['days_to_start_1'])
    elif row['start_subtask_2'] is not None and row['start_subtask_3'] is None:
        ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1']),
                                (row['days_to_start_2'], row['task_duration_2'])], yrange=(index + 1, 0.5))
    else:
        ax.broken_barh(
            xranges=[(row['days_to_start_1'], row['task_duration_1']), (row['days_to_start_2'], row['task_duration_2']),
                     (row['days_to_start_3'], row['task_duration_3'])], yrange=(index + 1, 0.5))

# 3
ax.set_yticks([1.25, 2.25, 3.25, 4.25])
ax.set_yticklabels(df_sales_subtask['task'])

plt.show()

plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.show()

# 1
fig, ax = plt.subplots()

plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'] + 1)
plt.title('Project Management Schedule of Project X', fontsize=15)

# 2
plt.gca().invert_yaxis()

# 3. Figure out the optimal locations of the x-ticks
x_ticks = np.arange(5, df['days_to_end'].max() + 2, 7)

# 4
x_tick_labels = pd.date_range(start=df['start'].min() + dt.timedelta(days=4), end=df['end'].max()).strftime("%d/%m")

# 5. Add the x-ticks and x-tick labels
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels[::7])

# 6. Add a vertical grid
ax.xaxis.grid(True, alpha=0.5)
plt.show()

# 1. Create a dictionary with the team names as its keys and base matplotlib colors as its values
team_colors = {'R&D': 'c', 'Accounting': 'm', 'Sales': 'y', 'IT': 'b'}

# 2. Create a figure with subplots
fig, ax = plt.subplots()

# 3.
for index, row in df.iterrows():
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

# 4. Iterate through the rows of the dataframe, create a bar for each row and add the color
# corresponding to the team
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels[::7])
ax.xaxis.grid(True, alpha=0.5)
plt.show()

patches = []
for team in team_colors:
    patches.append(matplotlib.patches.Patch(color=team_colors[team]))

fig, ax = plt.subplots()
for index, row in df.iterrows():
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']])
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels[::7])
ax.xaxis.grid(True, alpha=0.5)

# Adding a legend
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)

plt.show()

# Adding Status of Completion
fig, ax = plt.subplots()

for index, row in df.iterrows():

    # Adding a lower bar - for the overall task duration
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']], alpha=0.4)

    # Adding an upper bar - for the status of completion
    plt.barh(y=row['task'], width=row['completion_days'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels[::7])
ax.xaxis.grid(True, alpha=0.5)
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)
plt.show()

# current date is the 17 of November 2022 and mark this date on our chart
fig, ax = plt.subplots()
for index, row in df.iterrows():
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']], alpha=0.4)
    plt.barh(y=row['task'], width=row['completion_days'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels[::7])
ax.xaxis.grid(True, alpha=0.5)
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)

# Marking the current date on the chart
ax.axvline(x=29, color='r', linestyle='dashed')
ax.text(x=29.5, y=11.5, s='17/11', color='r')

plt.show()
