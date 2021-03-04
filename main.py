import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class Main:
	def __init__(self):
		gladeFile = "main.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(gladeFile)
		self.builder.connect_signals(self)

		#Connect window
		window = self.builder.get_object("window")
		window.connect("delete-event", gtk.main_quit)
		window.show()

		


	
	#Method called when search button is clicked in GUI
	def onSearchButtonClicked(self, widget):
			
			serachData = "";
			#get Text From Username Textbox
			userInputBox = self.builder.get_object("usernameEntryBox")
			#check if datafield is empty
			if(len(userInputBox.get_text())< 1):
				print("User Data Not Prestent")
			userText = userInputBox.get_text()
			serachData = "Username: " + userText + '\n'

			#get Text from Password Text Box
			passInputBox = self.builder.get_object("passwordEntryBox")
			#check if datafield is empty
			if(len(passInputBox.get_text())< 1):
				print("Password Data Not Prestent")				
			passText = passInputBox.get_text()
			serachData += "Password: " + passText + '\n'

			#get Text from Server TextBox
			serverInputBox = self.builder.get_object("serverEntryBox")
			#check if datafield is empty
			if(len(serverInputBox.get_text())< 1):
				print("Server data Not Prestent")
			serverText = serverInputBox.get_text()
			serachData += "Server: " + serverText + '\n'

			#Get Text from dates textbox with '/' removed
			startDateInputBox = self.builder.get_object("startDateEntryBox")
			#check if datafield is empty
			if(len(startDateInputBox.get_text())< 1):
				print("Start Date no Present")
			startDateText = startDateInputBox.get_text().replace("/","")
			serachData += "StartDate: " + startDateText + '\n'

			endDateInputBox = self.builder.get_object("endDateEntryBox")
			#check if datafield is empty
			if(len(endDateInputBox.get_text())< 1):
				print("End Date no Present")
			endDateText = endDateInputBox.get_text().replace("/","")
			serachData += "EndDate: " + endDateText + '\n'

			#pass that all dates available was selected. Grey out Start and end Dates

			#get type of field requested
			fieldSelectorBox = self.builder.get_object("fieldSelector")
			
			fieldText = fieldSelectorBox.get_active_text()
			serachData += "Fields Requested: " + fieldText


			#print
			print (serachData)



if __name__ == '__main__':
	main = Main()
	gtk.main()