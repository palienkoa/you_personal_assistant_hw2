# Your Personal Assistant

It's a Python application that provides functionality to manage an address book, take notes and sort any folder with mixed files. The application allows you to manage contact records, add and remove phone numbers and email addresses, manage birthdays and addresses, and search for records based on various criteria. Also, you can create and manage notes, add desired tags and search for notes by any keyword or tag. Finally, the application can sort any folder with different file types into  easily managable categories like images, video, documents etc.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)

## Features

### Address Book Management

- Create and manage contact records with the following information:
  - Name
  - Phone numbers
  - Email addresses
  - Birthday
  - Address
- Edit and delete contact records.
- Add, edit, or delete phone numbers and email addresses for a contact.
- Set or remove a birthday for a contact.
- Set or remove an address for a contact.
- Search for contact records based on a search string.
- List upcoming birthdays within a specified number of days.
- View all contact records.

- ### Notes Management

- Create and manage notes with content and tags.
- Search for words my any keyword in the title or the note itself.
- Search for notes by tags.
- View all notes.
- Edit or delete notes.

- ### Folder sorting

- Sort any "junk" folder into easily managable subcategory folders like IMAGES, VIDEOS, AUDIO, DOCUMENTS, ARCHIVES and OTHER

## Installation

 1. Download provided package file your_personal_assistant.zip
 2. Unzip the package
 3. Install the package, by navigating to the folder from previous step and running command: ```pip install .``` 

## Usage

1. Run the application by executing command ```my_assistant``` in the terminal.

## Commands
The application supports the following commands:

- add [Name]: Create a new contact record with the specified name.
- edit [Name] [new_Name]: Edit the name of a contact record.
- del [Name]: Remove a contact record.
- add-phone [Name] [Phone]: Add a phone number to a contact.
- edit-phone [Name] [Phone] [new_Phone]: Replace a phone number in a contact.
- del-phone [Name] [Phone]: Remove a phone number from a contact.
- add-email [Name] [Email]: Add an email address to a contact.
- edit-email [Name] [Email] [new_Email]: Replace an email address in a contact.
- del-email [Name] [Email]: Remove an email address from a contact.
- birthday [Name] [Birthday]: Set a birthday for a contact.
- del-birthday [Name]: Remove a birthday from a contact.
- address [Name] [Address]: Set an address for a contact.
- del-address [Name]: Remove an address from a contact.
- find [searchstring]: Search for contact records based on a search string.
- help: Display a list of available commands.
- add-note: Add a note to Note Book.
- all-notes: List all notes
- del-note [Note_title]: Remove note from Note Book
- add-tag [Note_id] [Tag]: Add tag to note
- del-tag [Note_id] [Tag]: Remove tag from note
- find-notes [searchstring]: List all notes with search string data in note and tags
- find-tag [searchstring]: List all notes with search string data in tags
- sort-tag: ???
- show-all-tags: Lists all saved tags
- next-birthdays [int]: Show upcoming birthdays within the specified number of days.
- show-all: List all contact records.
- close,exit or bye: Exit the application.