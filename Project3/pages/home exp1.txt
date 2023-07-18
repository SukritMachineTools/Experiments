from tkinter import *
from tkinter.ttk import Treeview
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import re
import datetime
import os
import csv

##########################
#   Configuration
bgcolor="#99ff99"
winH=768
winW=1366
winS=str(winW)+"x"+str(winH)
###########################
# Default Values
job='S.R. Shaft THD'
breakTime='01:30'
start_date= '2023-06-01'
end_date= '2023-07-07'
flag=0
targetv = 55
incentivev = 0.70
############################

class home:
    def __int__(self):
        pass
    def machinePage(self):
        self.root=Tk()
        self.root.geometry(winS)
        self.root.title("Sukrit Production Records")
        self.root.configure(background=bgcolor)

        #############################################################
        def intialFunc():
            pass


        ################MACHINE FUNCTION 1############################
        def machineFunc():
            try:
                # read google sheets
                df = pd.read_csv(
                    'https://docs.google.com/spreadsheets/d/e/2PACX-1vT6HrGh7EOzzejrvzkG_TGUM_GoGVDuvlUq7UcYqHlESZX6Vv8Hvwatsp4FLdE4Nmff9z5LSG3KQFq9/pub?gid=1362009325&single=true&output=csv')
            except:
                df=pd.read_csv('./production.csv')
            # renamed columns
            df.rename(columns={'Rejection': 'M/C', 'Unnamed: 6': 'CASTING',
                               'Unnamed: 7': 'OTHER', 'Timming': 'Start_Time', 'Unnamed: 11': 'End_Time',
                               'Total Prod': 'Total_Prod', 'Final Prod': 'Final_Prod', 'Total Rej': 'Total_Rej'},
                      inplace=True)
            df = df.drop(index=0)
            df = df.reset_index(drop=True)
            df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

            # Convert the 'time_string' column to time object
            df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M')
            df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M')

            # Calculate the time difference

            df['time_difference1'] = df['End_Time'] - df['Start_Time']
            df['time_difference1'] = df['time_difference1'] - pd.Timedelta(hours=1, minutes=30)
            df['time_difference'] = df['time_difference1'].apply(
                lambda x: '{:02d}:{:02d}'.format(int(x.seconds // 3600), int((x.seconds // 60) % 60)))

            df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M').dt.time
            df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M').dt.time
            df['time_difference'] = pd.to_datetime(df['time_difference'], format='%H:%M').dt.time

            # job = 'S.R. Shaft THD'
            # breakTime = '01:30'
            # start_date = '2023-06-01'
            # end_date = '2023-07-07'

            # mask = (df['date'] > start_date) & (df['date'] <= end_date)
            mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
            datedf = df.loc[mask]
            newdf = datedf[datedf['Job'] == job]
            newdf = newdf.reset_index(drop=True)
            total_time = newdf['time_difference1'].sum()
            # df=df.drop(['time_difference1'], axis=1)
            total_hours = total_time.total_seconds() / 3600
            newdf = newdf.astype(
                {'Total_Prod': 'int', 'M/C': 'int', 'CASTING': 'int', 'OTHER': 'int', 'Total_Rej': 'int',
                 'Final_Prod': 'int'})
            newdf['Date'] = newdf['Date'].dt.strftime('%d-%m-%Y')
            sumrow = {'Date': 'Total', 'Total_Prod': sum(newdf['Total_Prod']), 'M/C': sum(newdf['M/C']),
                      'CASTING': sum(newdf['CASTING']), 'OTHER': sum(newdf['OTHER']),
                      'Final_Prod': sum(newdf['Final_Prod']), 'time_difference': total_hours}
            sumrow = pd.DataFrame(sumrow, index=['Total'])
            newdf = pd.concat([newdf, sumrow], axis=0)
            machinedf = newdf.copy()
            machinedf = machinedf.drop(['time_difference1'], axis=1)
            machinedf = machinedf.fillna("...")

            return machinedf
            pass

        def operatorFunc():
            try:
                # read google sheets
                df = pd.read_csv(
                    'https://docs.google.com/spreadsheets/d/e/2PACX-1vT6HrGh7EOzzejrvzkG_TGUM_GoGVDuvlUq7UcYqHlESZX6Vv8Hvwatsp4FLdE4Nmff9z5LSG3KQFq9/pub?gid=1362009325&single=true&output=csv')
            except:
                df=pd.read_csv('./production.csv')

            # renamed columns
            df.rename(columns={'Rejection': 'M/C', 'Unnamed: 6': 'CASTING',
                               'Unnamed: 7': 'OTHER', 'Timming': 'Start_Time', 'Unnamed: 11': 'End_Time',
                               'Total Prod': 'Total_Prod', 'Final Prod': 'Final_Prod', 'Total Rej': 'Total_Rej'},
                      inplace=True)
            df = df.drop(index=0)
            df = df.reset_index(drop=True)
            df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

            # Convert the 'time_string' column to time object
            df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M')
            df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M')

            # Calculate the time difference

            df['time_difference1'] = df['End_Time'] - df['Start_Time']
            df['time_difference1'] = df['time_difference1'] - pd.Timedelta(hours=1, minutes=30)
            df['time_difference'] = df['time_difference1'].apply(
                lambda x: '{:02d}:{:02d}'.format(int(x.seconds // 3600), int((x.seconds // 60) % 60)))

            df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M').dt.time
            df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M').dt.time
            df['time_difference'] = pd.to_datetime(df['time_difference'], format='%H:%M').dt.time

            # job = 'S.R. Shaft THD'
            # breakTime = '01:30'
            # start_date = '2023-06-01'
            # end_date = '2023-07-07'

            # mask = (df['date'] > start_date) & (df['date'] <= end_date)
            mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
            datedf = df.loc[mask]
            newdf = datedf[datedf['Job'] == job]
            newdf = newdf.reset_index(drop=True)
            total_time = newdf['time_difference1'].sum()
            # df=df.drop(['time_difference1'], axis=1)
            total_hours = total_time.total_seconds() / 3600
            newdf = newdf.astype(
                {'Total_Prod': 'int', 'M/C': 'int', 'CASTING': 'int', 'OTHER': 'int', 'Total_Rej': 'int',
                 'Final_Prod': 'int'})
            newdf['Date'] = newdf['Date'].dt.strftime('%d-%m-%Y')
            sumrow = {'Date': 'Total', 'Total_Prod': sum(newdf['Total_Prod']), 'M/C': sum(newdf['M/C']),
                      'CASTING': sum(newdf['CASTING']), 'OTHER': sum(newdf['OTHER']),
                      'Final_Prod': sum(newdf['Final_Prod']),
                      'time_difference': total_hours}
            sumrow = pd.DataFrame(sumrow, index=['Total'])
            newdf = pd.concat([newdf, sumrow], axis=0)

            # Get the distinct values in a specific column
            distinct_values = newdf['Operator'].unique()  # Replace 'column_name' with the actual column name

            distinct_values = list(distinct_values)
            distinct_values.pop()
            days = []
            total_hours = []
            sum_prod = []
            sum_mc = []
            sum_cast = []
            sum_other = []
            sum_finalprod = []
            avg_hourly = []
            avg_day = []
            for i in range(len(distinct_values)):
                op1 = newdf[newdf['Operator'] == distinct_values[i]]
                daysop = op1.shape[0]
                days.append(daysop)
                total_timeop = op1['time_difference1'].sum()
                total_hoursop = round((total_timeop.total_seconds() / 3600), 2)
                total_hours.append(total_hoursop)
                sum_prodop = sum(op1['Total_Prod'])
                sum_prod.append(sum_prodop)
                sum_mcop = sum(op1['M/C'])
                sum_mc.append(sum_mcop)
                sum_castop = sum(op1['CASTING'])
                sum_cast.append(sum_castop)
                sum_otherop = sum(op1['OTHER'])
                sum_other.append(sum_otherop)
                sum_finalprodop = sum(op1['Final_Prod'])
                sum_finalprod.append(sum_finalprodop)
                avg_hourlyop = round((sum_prodop / total_hoursop), 2)
                avg_hourly.append(avg_hourlyop)
                avg_dayop = round((sum_prodop / daysop), 2)
                avg_day.append(avg_dayop)
            product = {
                'Operator': distinct_values,
                'DAYS': days,
                'HOURS': total_hours,
                'Total_Prod': sum_prod,
                'M/C': sum_mc,
                'Casting': sum_cast,
                'Other': sum_other,
                'Final_Prod': sum_finalprod,
                'Hourly_Avg': avg_hourly,
                'Day_Avg': avg_day
            }
            print(product)
            prod_df = pd.DataFrame(product)
            prod_df['Deduct_Machine_rej'] = prod_df['Total_Prod'] - prod_df['M/C']
            prod_df['Deduct_Machine_rej'] = prod_df['Deduct_Machine_rej'].round(2)
            # targetv = 55
            # incentivev = 0.70
            prod_df['Hours X Target'] = prod_df['HOURS'] * targetv
            prod_df['Hours X Target'] = prod_df['Hours X Target'].round(2)
            prod_df['Extra Prod'] = prod_df['Deduct_Machine_rej'] - prod_df['Hours X Target']
            prod_df['Extra Prod'] = prod_df['Extra Prod'].round(2)
            prod_df['Incentive'] = prod_df['Extra Prod'] * incentivev
            prod_df['Incentive'] = prod_df['Incentive'].round(2)

            sumrow2 = {'Operator': 'Total', 'DAYS': sum(prod_df['DAYS']), 'HOURS': sum(prod_df['HOURS']),
                       'Total_Prod': sum(prod_df['Total_Prod']), 'M/C': sum(prod_df['M/C']),
                       'Casting': sum(prod_df['Casting']),
                       'Other': sum(prod_df['Other']), 'Final_Prod': sum(prod_df['Final_Prod']),
                       'Hourly_Avg': round(sum(prod_df['Hourly_Avg']), 2), 'Day_Avg': round(sum(prod_df['Day_Avg']), 2),
                       'Deduct_Machine_rej': round(sum(prod_df['Deduct_Machine_rej']), 2),
                       'Hours X Target': round(sum(prod_df['Hours X Target']), 2),
                       'Extra Prod': round(sum(prod_df['Extra Prod']), 2),
                       'Incentive': round(sum(prod_df['Incentive']), 2)}
            sumrow2 = pd.DataFrame(sumrow2, index=['Total'])
            operatordf = pd.concat([prod_df, sumrow2], axis=0)

            return (operatordf,newdf)

        def monthlyFunc():
            try:
                # read google sheets
                df = pd.read_csv(
                    'https://docs.google.com/spreadsheets/d/e/2PACX-1vT6HrGh7EOzzejrvzkG_TGUM_GoGVDuvlUq7UcYqHlESZX6Vv8Hvwatsp4FLdE4Nmff9z5LSG3KQFq9/pub?gid=1362009325&single=true&output=csv')
            except:
                df=pd.read_csv('./production.csv')
            # renamed columns
            df.rename(columns={'Rejection': 'M/C', 'Unnamed: 6': 'CASTING',
                               'Unnamed: 7': 'OTHER', 'Timming': 'Start_Time', 'Unnamed: 11': 'End_Time',
                               'Total Prod': 'Total_Prod', 'Final Prod': 'Final_Prod', 'Total Rej': 'Total_Rej'},
                      inplace=True)
            df = df.drop(index=0)
            df = df.reset_index(drop=True)
            df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

            # Convert the 'time_string' column to time object
            df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M')
            df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M')

            # Calculate the time difference

            df['time_difference1'] = df['End_Time'] - df['Start_Time']
            df['time_difference1'] = df['time_difference1'] - pd.Timedelta(hours=1, minutes=30)
            df['time_difference'] = df['time_difference1'].apply(
                lambda x: '{:02d}:{:02d}'.format(int(x.seconds // 3600), int((x.seconds // 60) % 60)))

            df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M').dt.time
            df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M').dt.time
            df['time_difference'] = pd.to_datetime(df['time_difference'], format='%H:%M').dt.time

            # job='S.R. Shaft THD'
            # breakTime='01:30'
            start_date = '2023-06-01'
            end_date = '2023-07-07'

            # mask = (df['date'] > start_date) & (df['date'] <= end_date)
            mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
            datedf = df.loc[mask]
            newdf = datedf[datedf['Job'] == job]
            newdf = newdf.reset_index(drop=True)
            total_time = newdf['time_difference1'].sum()
            # df=df.drop(['time_difference1'], axis=1)
            total_hours = total_time.total_seconds() / 3600
            newdf = newdf.astype(
                {'Total_Prod': 'int', 'M/C': 'int', 'CASTING': 'int', 'OTHER': 'int', 'Total_Rej': 'int',
                 'Final_Prod': 'int'})
            newdf['Date'] = newdf['Date'].dt.strftime('%d-%m-%Y')
            sumrow = {'Date': 'Total', 'Total_Prod': sum(newdf['Total_Prod']), 'M/C': sum(newdf['M/C']),
                      'CASTING': sum(newdf['CASTING']), 'OTHER': sum(newdf['OTHER']),
                      'Final_Prod': sum(newdf['Final_Prod']), 'time_difference': total_hours}
            sumrow = pd.DataFrame(sumrow, index=['Total'])
            newdf = pd.concat([newdf, sumrow], axis=0)

            # Get the distinct values in a specific column
            distinct_values_Job = df['Job'].unique()
            distinct_values_Job = list(distinct_values_Job)
            distinct_values_Job.pop()

            # multi table
            machinej = []
            t_prodj = []
            mcj = []
            castj = []
            otherj = []
            final = []
            column_names = ['Machines', 'PRODUCT', 'Total_Prod', 'M/C', 'CASTING', 'OTHER', 'FINAL']
            dflist = []
            # Create an empty dataframe with the specified column names
            jobs = pd.DataFrame(columns=column_names)

            for j in range(len(distinct_values_Job)):
                job1 = df[df['Job'] == distinct_values_Job[j]]
                job1 = job1.loc[mask]
                job1 = job1.reset_index(drop=True)
                job1 = job1.astype(
                    {'Total_Prod': 'int', 'M/C': 'int', 'CASTING': 'int', 'OTHER': 'int', 'Total_Rej': 'int',
                     'Final_Prod': 'int'})
                distinct_values_Mc = job1['Machines'].unique()
                distinct_values_Mc = list(distinct_values_Mc)

                jobs = pd.DataFrame(columns=column_names)

                for m in range(len(distinct_values_Mc)):
                    job2 = job1[job1['Machines'] == distinct_values_Mc[m]]
                    job2 = job2.astype(
                        {'Total_Prod': 'int', 'M/C': 'int', 'CASTING': 'int', 'OTHER': 'int', 'Total_Rej': 'int',
                         'Final_Prod': 'int'})
                    job3 = {'Machines': distinct_values_Mc[m], 'PRODUCT': distinct_values_Job[j],
                            'Total_Prod': sum(job2['Total_Prod']), 'M/C': sum(job2['M/C']),
                            'CASTING': sum(job2['CASTING']), 'OTHER': sum(job2['OTHER']),
                            'FINAL': sum(job2['Final_Prod'])}
                    job3 = pd.DataFrame(job3, index=[m])
                    jobs = pd.concat([jobs, job3], ignore_index=True)
                job3 = {'Machines': 'Total', 'PRODUCT': '...', 'Total_Prod': sum(jobs['Total_Prod']),
                        'M/C': sum(jobs['M/C']), 'CASTING': sum(jobs['CASTING']), 'OTHER': sum(jobs['OTHER']),
                        'FINAL': sum(jobs['FINAL'])}
                job3 = pd.DataFrame(job3, index=[0])
                jobs = pd.concat([jobs, job3], ignore_index=True)
                dflist.append(jobs)


            return dflist

        def exportmonthly(df_list):
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            file_path = filedialog.asksaveasfilename(initialdir=downloads_path,
                                                     defaultextension=".csv",
                                                     filetypes=(("CSV files", "*.csv"), ("text files", "*.txt"),
                                                                ("All files", "*.*")))
            if file_path:
                # Perform saving operations with the selected file path
                print("Selected file path:", file_path)
            # Export the DataFrame to a CSV file with headers
            for dframe in df_list:
                print(type(df_list))
                dframe.to_csv(file_path, mode='a', header=True, index=False)
            pass

        def exportcsv(dataframe):
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            file_path = filedialog.asksaveasfilename(initialdir=downloads_path,
                                                     defaultextension=".csv",
                                                     filetypes=(("CSV files", "*.csv"),("text files", "*.txt"), ("All files", "*.*")))
            if file_path:
                # Perform saving operations with the selected file path
                print("Selected file path:", file_path)
            # Export the DataFrame to a CSV file with headers
            dataframe.to_csv(file_path, index=False)
            pass


        #########format check#########################################
        def check_date_format(input_string):
            pattern = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern, input_string):
                return input_string
            else:
                err="Error"
                return err

        def check_btime_format(input_string):
            pattern = r'^\d{1}:\d{2}$'
            pattern2 = r'^$'
            if re.match(pattern, input_string):
                return input_string
            elif re.match(pattern2, input_string):
                input_string=breakTime
                return input_string
            else:
                err="Error"
                return err

        #######SWITCH PAGES########################################################
        def mactoOpPage():
            frame2.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()
            Operatorpage()

        def mactoMoPage():
            frame2.destroy()
            frame2i.destroy()
            frame3.destroy()
            frame4.destroy()
            frame5.destroy()
            frame6.destroy()
            monthlyPage()

        def hometoMoPage():
            global job
            global breakTime
            global start_date
            global end_date
            global incentivev
            global targetv
            flag = 0

            if (jobvalue.get()) !="Select an option":
                job = jobvalue.get()
                print(job)
            # else:
            #     print("job error")
            #     messagebox.showerror("Error", "Enter the Job")
            #     flag = 1

            if check_btime_format(bTimevalue.get()) != "Error":
                breakTime = check_btime_format(bTimevalue.get())
                print(breakTime)
            else:
                print("btime error")
                messagebox.showerror("Error", "Enter correct Break Time")
                flag = 1
            if check_date_format(sDatevalue.get()) != "Error":
                start_date = check_date_format(sDatevalue.get())
                print(start_date)
            else:
                print("st date error")
                messagebox.showerror("Error", "Enter correct Start Date")
                flag = 1
            if check_date_format(eDatevalue.get()) != "Error":
                end_date = check_date_format(eDatevalue.get())
                print(end_date)
            else:
                print("end date error")
                messagebox.showerror("Error", "Enter correct End Date")
                flag = 1
            if (targetvalue.get()).isdigit():
                if int(targetvalue.get()) > 0:
                    targetv = int(targetvalue.get())
                else:
                    messagebox.showerror("Error", "Enter valid target")
                    flag = 1
            elif (re.match(r'^$', targetvalue.get())):
                pass
            else:
                messagebox.showerror("Error", "Enter valid target")
                flag = 1

            if re.match(r'^[-+]?[0-9]*\.[0-9]+$', incentivevalue.get()):
                incentivev = float(incentivevalue.get())
            elif (re.match(r'^$', incentivevalue.get())):
                pass
            else:
                messagebox.showerror("Error", "Enter valid incentive")
                flag = 1

            if flag != 1:
                frame2.destroy()
                frame3.destroy()
                frame4.destroy()
                monthlyPage()


        #########Monthly Page#######################################################
        def monthlyPage():
            # global frame5
            # global frame6
            # global frame2i




            frame2 = Frame(self.root, bg="blue", height=15)
            Label(frame2, text="Monthly Production", fg="#ffffff", font="Algerian 20 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=0,
                column=1, sticky='n')
            frame2i = Frame(frame2, highlightbackground="blue", width=300, height=100, highlightthickness=1, bg=bgcolor)
            Label(frame2i, text="Start Date:", fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=1)
            Label(frame2i, text=start_date, fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=2)
            Label(frame2i, text="End Date:", fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=3)
            Label(frame2i, text=end_date, fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=4)

            frame2i.grid(row=1, column=1, ipadx=33.5, sticky="w")
            frame2.grid(row=1, ipadx=400, sticky='ew')

            frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=2,
                           bg=bgcolor)
            datalist=monthlyFunc()

            if len(datalist)>0:
                # Create a scrollbar
                scrollBar = Scrollbar(frame3)
                scrollBar.grid(row=0, column=1, sticky="ns")
                # Configure the scrollbar to work with the Treeview widget
                # scrollBar.config(command=treeview.yview)
                frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0,
                               bg=bgcolor)


                frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")
                for i, dataframe in enumerate(datalist):
                    # Create a new frame for each dataframe
                    frame = Frame(frame4)
                    frame.grid(row=i)
                    # Create a Treeview widget
                    treeview = Treeview(frame,yscrollcommand=scrollBar.set,height=5)
                    treeview["columns"] = list(dataframe.columns)
                    treeview["show"] = "headings"

                    # Add columns to the Treeview
                    for column in dataframe.columns:
                        treeview.heading(column, text=column)
                        treeview.column(column, width=100)

                    # Add rows to the Treeview
                    for row in dataframe.itertuples(index=False):
                        treeview.insert("", "end", values=row)

                    # Add a vertical scrollbar to the Treeview
                    scrollbar = Scrollbar(frame, orient="vertical", command=treeview.yview)
                    treeview.configure(yscroll=scrollbar.set)

                    # Grid layout configuration within the Frame
                    treeview.grid(row=0, column=0, sticky="nsew")
                    scrollbar.grid(row=0, column=1, sticky="ns")
                    scrollBar.config(command=treeview.yview)

                    # Configure grid weights within the Frame to resize properly
                    frame.grid_rowconfigure(0, weight=1)
                    frame.grid_columnconfigure(0, weight=1)






            else:
                frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0,
                               bg=bgcolor)
                # Cooper Black
                searchJob = job + " : Not Found"
                Label(frame4, text=searchJob, font="Stencil 26 bold", padx=7, pady=7, bg=bgcolor,
                      fg="red").grid(row=0, column=0)
                frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")




            frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")

            frame5 = Frame(self.root, bg="blue", height=10)
            # wlabel=Label(frame2,text="",bg="blue",height=10).grid(row=1)
            frame5.grid(row=3, ipadx=400, sticky='ew')

            frame6 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg=bgcolor)
            Button(frame6, text="Export to CSV",command=lambda: exportmonthly(datalist), padx=30, bg="#ffcc99",
                   fg="#000000").grid(row=0, column=0, padx=20, pady=10)
            Button(frame6, text="Operator Report", command=mactoOpPage, padx=30, bg="#ffcc99", fg="#000000").grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=20,
                                                                                                                  pady=10)
            Button(frame6, text="Monthly Report", padx=30, bg="#ffcc99", fg="#000000").grid(row=0,
                                                                                                                 column=2,
                                                                                                                 padx=20,
                                                                                                                 pady=10)
            Button(frame6, text="Settings", padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=3, padx=20, pady=10)
            frame6.grid(row=4, ipadx=20, sticky='ew')
            pass


        ###########OPERATOR PAGE#####################################################
        def Operatorpage():
            frame2 = Frame(self.root, bg="blue", height=15)
            Label(frame2, text="Operator's Records", fg="#ffffff", font="Elephant 20 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=0,
                column=1, sticky='n')
            frame2i = Frame(frame2, highlightbackground="blue", width=300, height=100, highlightthickness=1, bg=bgcolor)
            Label(frame2i, text="Start Date:", fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=1)
            Label(frame2i, text=start_date, fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=2)
            Label(frame2i, text="End Date:", fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=3)
            Label(frame2i, text=end_date, fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=4)
            Label(frame2i, text="Job:", fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=5)
            Label(frame2i, text=job, fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=6)
            Label(frame2i, text="Break Time:", fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=7)
            Label(frame2i, text=breakTime, fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=8)
            Label(frame2i, text="Target:", fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=9)
            Label(frame2i, text=targetv, fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=10)
            Label(frame2i, text="Incentive:", fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=11)
            Label(frame2i, text=incentivev, fg="#000000", font="Algerian 14 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=12)
            frame2i.grid(row=1, column=1, ipadx=33.5, sticky="w")
            frame2.grid(row=1, ipadx=400, sticky='ew')

            frame3 = Frame(self.root, highlightbackground="blue", width=winW, height=100, highlightthickness=2,
                           bg=bgcolor)
            operatordf,newdf=operatorFunc()
            element = job
            # Search for the element in the specified column
            is_present = element in newdf['Job'].values

            # Print the result
            if is_present:
                print(f"The element '{element}' is present in the '{'Job'}' column.")
                frame4 = Frame(frame3, highlightbackground="blue", width=winW, height=100, highlightthickness=0,
                               bg=bgcolor)

                dataframe = operatordf
                # Create a canvas
                canvas = Canvas(frame4,bg=bgcolor,width=winW)
                canvas.grid(row=0, column=0, sticky='nsew')

                # Add a horizontal scrollbar
                scrollbar = Scrollbar(frame4, orient='horizontal', command=canvas.xview)
                scrollbar.grid(row=1, column=0, sticky='ew')
                canvas.configure(xscrollcommand=scrollbar.set)

                # Create a frame inside the canvas
                df_frame = Frame(canvas,bg=bgcolor)
                canvas.create_window((0, 0), window=df_frame, anchor='nw',width=winW)

                # Create a Pandas DataFrame table within the frame
                table = Treeview(df_frame, columns=list(operatordf.columns), show='headings')
                table.grid(row=0, column=0, sticky='nsew')

                # Insert column headers
                for column in operatordf.columns:
                    table.heading(column, text=column)

                # Insert data rows
                for _, row in operatordf.iterrows():
                    table.insert('', 'end', values=list(row))

                # Decrease the width of all columns
                for column in operatordf.columns:
                    table.column(column, width=80)  # Specify the desired width
                # Configure the grid weights
                # self.root.grid_rowconfigure(0, weight=1)
                # self.root.grid_columnconfigure(0, weight=1)
                frame4.grid_rowconfigure(0, weight=1)
                frame4.grid_columnconfigure(0, weight=1)
                df_frame.grid_rowconfigure(0, weight=1)
                df_frame.grid_columnconfigure(0, weight=1)

                # Update the canvas scrolling region
                canvas.update_idletasks()
                canvas.configure(scrollregion=canvas.bbox('all'))

                frame4.grid(row=0, column=0, sticky="w")

            else:
                print(f"The element '{element}' is not present in the '{'Job'}' column.")
                frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0,
                               bg=bgcolor)
                # Cooper Black
                searchJob = job + " : Not Found"
                Label(frame4, text=searchJob, font="Stencil 26 bold", padx=7, pady=7, bg=bgcolor,
                      fg="red").grid(row=0, column=0)
                frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")

            frame3.grid(row=2, column=0, ipadx=13.5, sticky="ew")

            frame5 = Frame(self.root, bg="blue", height=10)
            # wlabel=Label(frame2,text="",bg="blue",height=10).grid(row=1)
            frame5.grid(row=3, ipadx=400, sticky='ew')

            frame6 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg=bgcolor)
            Button(frame6, text="Export to CSV", command=lambda: exportcsv(operatordf), padx=30, bg="#ffcc99",
                   fg="#000000").grid(row=0, column=0, padx=20, pady=10)
            Button(frame6, text="Machine Report", padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=1, padx=20,
                                                                                             pady=10)
            Button(frame6, text="Monthly Report", padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=2, padx=20,
                                                                                            pady=10)
            Button(frame6, text="Settings", padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=3, padx=20, pady=10)
            frame6.grid(row=4, ipadx=20, sticky='ew')
            pass

        ###########MACHINE PAGE########################################################
        # Machine Frame
        def mpage():
            global frame2
            global frame3
            global frame4
            global frame5
            global frame6
            global frame2i
            frame2 = Frame(self.root, bg="blue", height=15)
            Label(frame2, text="Production Records", fg="#ffffff", font="Algerian 20 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=0,
                column=1, sticky='n')
            frame2i = Frame(frame2, highlightbackground="blue", width=300, height=100, highlightthickness=1, bg=bgcolor)
            Label(frame2i, text="Start Date:", fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=1)
            Label(frame2i, text=start_date, fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=2)
            Label(frame2i, text="End Date:", fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=3)
            Label(frame2i, text=end_date, fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=4)
            Label(frame2i, text="Job:", fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=5)
            Label(frame2i, text=job, fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=6)
            Label(frame2i, text="Break Time:", fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=1,
                column=7)
            Label(frame2i, text=breakTime, fg="#000000", font="Elephant 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=8)
            frame2i.grid(row=1, column=1, ipadx=33.5, sticky="w")
            frame2.grid(row=1, ipadx=400, sticky='ew')

            frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=2,
                           bg=bgcolor)
            machinedf = machineFunc()
            element =job
            # Search for the element in the specified column
            is_present = element in machinedf['Job'].values

            # Print the result
            if is_present:
                print(f"The element '{element}' is present in the '{'Job'}' column.")
                frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0,
                               bg=bgcolor)

                dataframe = machinedf
                # Create a Treeview widget
                treeview = Treeview(frame4)
                treeview["columns"] = list(dataframe.columns)
                treeview["show"] = "headings"

                # Add columns to the Treeview
                for column in dataframe.columns:
                    treeview.heading(column, text=column)
                    treeview.column(column, width=100)

                # Add rows to the Treeview
                for row in dataframe.itertuples(index=False):
                    treeview.insert("", "end", values=row)

                # Add a vertical scrollbar to the Treeview
                scrollbar = Scrollbar(frame4, orient="vertical", command=treeview.yview)
                treeview.configure(yscroll=scrollbar.set)

                # Grid layout configuration
                treeview.grid(row=0, column=0, sticky="nsew")
                scrollbar.grid(row=0, column=1, sticky="ns")

                # Configure grid weights to resize properly
                frame4.grid_rowconfigure(0, weight=1)
                frame4.grid_columnconfigure(0, weight=1)

                frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")

            else:
                print(f"The element '{element}' is not present in the '{'Job'}' column.")
                frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0,
                               bg=bgcolor)
                # Cooper Black
                searchJob=job+" : Not Found"
                Label(frame4, text=searchJob, font="Stencil 26 bold", padx=7, pady=7, bg=bgcolor,
                      fg="red").grid(row=0, column=0)
                frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")

            frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")

            frame5 = Frame(self.root, bg="blue", height=10)
            # wlabel=Label(frame2,text="",bg="blue",height=10).grid(row=1)
            frame5.grid(row=3, ipadx=400, sticky='ew')

            frame6 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg=bgcolor)
            Button(frame6, text="Export to CSV", command=lambda: exportcsv(machinedf), padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=0, padx=20, pady=10)
            Button(frame6, text="Operator Report",command=mactoOpPage, padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=1, padx=20, pady=10)
            Button(frame6, text="Monthly Report",command=mactoMoPage , padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=2, padx=20, pady=10)
            Button(frame6, text="Settings", padx=30, bg="#ffcc99", fg="#000000").grid(row=0, column=3, padx=20, pady=10)
            frame6.grid(row=4,ipadx=20,sticky='ew')

            pass

        def on_select(event):
            job = jobvalue.get()
            # print(f"Selected value: {selected_value}")



        def submitD():
            global job
            global breakTime
            global start_date
            global end_date
            global incentivev
            global targetv
            flag=0

            # if len(jobvalue.get()) > 0:
            #     job=jobvalue.get()
            #     print(job)
            # else:
            #     print("job error")
            #     messagebox.showerror("Error", "Enter the Job")
            #     flag=1
            if (jobvalue.get()) !="Select an option":
                job = jobvalue.get()
                print(job)
            else:
                print("job error")
                messagebox.showerror("Error", "Enter the Job")
                flag = 1


            if check_btime_format(bTimevalue.get()) !="Error":
                breakTime=check_btime_format(bTimevalue.get())
                print(breakTime)
            else:
                print("btime error")
                messagebox.showerror("Error", "Enter correct Break Time")
                flag=1
            if check_date_format(sDatevalue.get()) != "Error":
                start_date=check_date_format(sDatevalue.get())
                print(start_date)
            else:
                print("st date error")
                messagebox.showerror("Error", "Enter correct Start Date")
                flag=1
            if check_date_format(eDatevalue.get()) !="Error":
                end_date=check_date_format(eDatevalue.get())
                print(end_date)
            else:
                print("end date error")
                messagebox.showerror("Error", "Enter correct End Date")
                flag=1
            if (targetvalue.get()).isdigit():
                if int(targetvalue.get())>0:
                    targetv=int(targetvalue.get())
                else:
                    messagebox.showerror("Error", "Enter valid target")
                    flag=1
            elif (re.match(r'^$', targetvalue.get())):
                pass
            else:
                messagebox.showerror("Error", "Enter valid target")
                flag = 1

            if re.match(r'^[-+]?[0-9]*\.[0-9]+$', incentivevalue.get()):
                incentivev=float(incentivevalue.get())
            elif (re.match(r'^$', incentivevalue.get())):
                pass
            else:
                messagebox.showerror("Error", "Enter valid incentive")
                flag = 1

            if flag!=1:
                frame2.destroy()
                frame3.destroy()
                frame4.destroy()
                mpage()
            pass

        #################################################################################################

        global job
        global breakTime
        global start_date
        global end_date



        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=1, bg=bgcolor)
        Label(frame1, text="Su", fg="#ffffff", font="Algerian 27 bold", padx=7, pady=7, bg="#000000").grid(
            row=0,
            column=1)
        Label(frame1, text="krit", fg="#000000", font="Algerian 27 bold", padx=7, pady=7, bg="#ffffff").grid(
            row=0,
            column=2)
        frame1.grid(row=0, ipadx=600, sticky="ew")
        frame2 = Frame(self.root, bg="blue", height=15)
        Label(frame2, text="Production Soft", fg="#ffffff", font="Algerian 20 bold", padx=7, pady=7, bg="blue").grid(
            row=0,
            column=1,sticky='n')
        Label(frame2, text="Monthly Record", fg="#000000", font="Algerian 16 bold", padx=7, pady=7, bg=bgcolor).grid(
            row=1,
            column=0, sticky='n')
        frame2.grid(row=1, ipadx=400, sticky='ew')
        frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=2, bg=bgcolor)

        frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0, bg=bgcolor)
        Label(frame4, text="ENTER THE DETAILS", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=0, column=0)
        Label(frame4, text="Start Date", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=1, column=0)
        sDatevalue = StringVar()
        Entry(frame4, width=10, textvariable=sDatevalue, font="Arial_Black 12 bold", ).grid(row=1, column=1)
        Label(frame4, text="(YYYY-MM-DD)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=2, column=0)
        Label(frame4, text="End Date", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=3, column=0)
        eDatevalue = StringVar()
        Entry(frame4, width=10, textvariable=eDatevalue, font="Arial_Black 12 bold", ).grid(row=3, column=1)
        Label(frame4, text="(YYYY-MM-DD)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=4, column=0)
        Label(frame4, text="Job", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=1, column=3)
        # jobvalue = StringVar()
        prdf = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vT6HrGh7EOzzejrvzkG_TGUM_GoGVDuvlUq7UcYqHlESZX6Vv8Hvwatsp4FLdE4Nmff9z5LSG3KQFq9/pub?gid=700061257&single=true&output=csv")
        jobdf = prdf['Job']
        jobdf.dropna(inplace=True)
        joblist = list(jobdf)
        jobvalue=ttk.Combobox(frame4, values=joblist)
        jobvalue.grid(row=1, column=4)
        jobvalue.set("Select an option")
        jobvalue.bind("<<ComboboxSelected>>", on_select)
        # Entry(frame4, width=20, textvariable=jobvalue, font="Arial_Black 12 bold", ).grid(row=1, column=4)
        Label(frame4, text="Break Time", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=3, column=3)
        bTimevalue = StringVar()
        Entry(frame4, width=20, textvariable=bTimevalue, font="Arial_Black 12 bold", ).grid(row=3, column=4)
        Label(frame4, text="(1:30)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=4, column=3)
        # Label(frame4, text="||", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
        #       fg="blue").grid(row=1, column=4)
        # Label(frame4, text="||", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
        #       fg="#000000").grid(row=2, column=4)
        # Label(frame4, text="||", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
        #       fg="blue").grid(row=3, column=4)
        # Label(frame4, text="||", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
        #       fg="#000000").grid(row=4, column=4)
        Label(frame4, text="Target", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=1, column=5)
        targetvalue = StringVar()
        Entry(frame4, width=20, textvariable=targetvalue, font="Arial_Black 12 bold", ).grid(row=1, column=6)
        Label(frame4, text="(55)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=2, column=5)
        Label(frame4, text="Incentive", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=3, column=5)
        incentivevalue = StringVar()
        Entry(frame4, width=20, textvariable=incentivevalue, font="Arial_Black 12 bold", ).grid(row=3, column=6)
        Label(frame4, text="(0.70)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=4, column=5)
        Button(frame4, command=submitD, text="SUBMIT", padx=30, bg="blue", fg="white").grid(row=5, column=1)
        Button(frame4, command=hometoMoPage, text="Monthly Report", padx=30, bg="blue", fg="white").grid(row=5, column=4)
        frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")

        frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")












        self.root.mainloop()

if __name__ == '__main__':
    pg = home()
    pg.machinePage()