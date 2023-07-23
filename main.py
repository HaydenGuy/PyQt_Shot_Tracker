import sys, os.path
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem

from UI.shot_tracker_ui import Ui_shot_tracker

# Taken from the Google quickstart python guide
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID of the spreadsheet.
SPREADSHEET_ID = '1qORbraCg2K5LvqwES8syIKsyIaSkpD-3UjwNGWXXRTI'


class ShotTracker(QMainWindow, Ui_shot_tracker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # creates a model item which will display the text we pull from the spreadsheet
        self.item_model = QStandardItemModel()
        

        # Taken from the Google quickstart python guide
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('Shot_Tracker/token.json'):
            creds = Credentials.from_authorized_user_file('Shot_Tracker/token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'Shot_Tracker/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('Shot_Tracker/token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            # Taken from the Google quickstart python guide
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()

            '''
                Initialise a column titles variable which gets the values of the spreadsheet from range A1:G1
                Assigns those values to a list called column title values
                Sets the number of columns in item model to be equal to the length of the list of items
            '''
            column_titles = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                            range='Sheet1!A1:G1').execute()
            column_title_values = column_titles.get('values', [])
            self.item_model.setColumnCount(len(column_title_values[0]))

            '''
                Creates an empty list which will be used to set the header labels
                Nested for loop that takes each of the items in the nested list and adds its value to the header labels list
                The header labels are set to the values in the list
            '''
            header_labels = []

            for column in column_title_values:
                for title in column:
                    header_labels.append(title)

            self.item_model.setHorizontalHeaderLabels(header_labels)

            '''
                Initialise a row info variable which gets the values of the spreadsheet from range A2:G11
                Assigns those values to a list called row info values
            '''
            row_info = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                            range='Sheet1!A2:G11').execute()
            row_info_values = row_info.get('values', [])

            '''
                This pulls the data from the spreadsheet and populates the item model
                Enumerate gets the index and the value of whatever it's iterating over
                We iterate over the nested list to retrieve one list at a time
                We iterate over the single list to retrieve its values
                The values are assigned to a QStandardItem
                The item model at row(i), column(i), is set to the item(i)
            '''
            for row, info in enumerate(row_info_values):
                for column, title in enumerate(info):
                    item = QStandardItem(title)
                    self.item_model.setItem(row, column, item)

            # the tree view is set to display the model item model
            self.tree_view.setModel(self.item_model)

        except HttpError as err:
            print(err)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ShotTracker()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())