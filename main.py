import openpyxl


def main():
    wb = openpyxl.load_workbook('healthcare.xlsx')
    sheet = wb.active

    user_data = {}

    for row in sheet.iter_rows():
        data_arr = []
        for cell in row:
            if cell.value is not None and cell.value != "":
                data_arr.append(cell.value)
        
        if len(data_arr) >= 4:
            user_id = data_arr[1]
            if user_id not in user_data:
                user_data[user_id] = {'data': [
                    [data_arr[0], data_arr[2]]
                ]}
            else:
                our_data = user_data[user_id]['data']
                our_data.append([data_arr[0], data_arr[2]])
                user_data[user_id]['data'] = our_data
            
                """
                previous_data = user_data[user_id]['data']
                updated_data = previous_data.append(
                    [data_arr[0], data_arr[2]]
                )
                user_data[user_id]['data'] = updated_data
                """

    file_obj = open("healthdata.txt", "w")
    all_user_details = ""
    for key, value in user_data.items():
        user_id = key
        intents = user_data[key]['data']
        list_of_intents_and_dates = ""
        for intent in intents:
            date = intent[0]
            intention = intent[1]
            a = f"{date} - {intention} \n"
            list_of_intents_and_dates += a
        
        user_details = user_id + '\n' + list_of_intents_and_dates + "\n \n"
        all_user_details += user_details
    
    file_obj.write(all_user_details)
    file_obj.close()




main()
