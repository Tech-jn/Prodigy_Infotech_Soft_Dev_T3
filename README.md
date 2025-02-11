# Prodigy_Infotech_Soft_Dev_T3
<h3>This is based on storing contact  information </h3>
<h5>This code implements a Contact Manager application with a graphical user interface using Python's tkinter library. Here's a detailed breakdown of its functionality:</h5>

1. Core Features:
- Add new contacts
- Edit existing contacts
- Delete contacts
- Persistent storage using JSON file
- Visual display of all contacts in a listbox

2. Data Management:
- Contacts are stored in a JSON file ("contacts.json")
- Each contact has three fields:
  - Name
  - Phone number
  - Email address
- Functions for loading (`load_contacts()`) and saving (`save_contacts()`) data
- Data persists between application sessions

3. GUI Components:
- Main window with title "Contact Manager"
- Black background theme
- Large listbox displaying all contacts
- Three action buttons with distinct colors:
  - Add Contact (Green)
  - Edit Contact (Blue)
  - Delete Contact (Red)

4. Functionality Details:

a) Adding Contacts:
- Clicking "Add Contact" opens dialog boxes for:
  - Name input
  - Phone number input
  - Email address input
- Validates that all fields are filled
- Shows success/warning messages

b) Editing Contacts:
- Must select a contact first
- Pre-fills existing information
- Opens dialog boxes for editing each field
- Validates all fields
- Shows success/warning messages

c) Deleting Contacts:
- Must select a contact first
- Removes the selected contact
- Updates the display immediately
- Shows confirmation/warning messages

5. User Interface Features:
- Clean, organized layout
- Easy-to-read contact list
- Light blue selection highlight
- Contrasting colors for better visibility
- Responsive feedback through message boxes

To use this application:
1. Run the program
2. The main window appears with any existing contacts
3. Use the buttons to manage contacts:
   - Green button to add new contacts
   - Blue button to edit selected contacts
   - Red button to delete selected contacts
