from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import datetime
from TOKEN import TOKEN

def get_notebook_guid(target_name, noteStore):
    notebooks = noteStore.listNotebooks()
    for current_note in notebooks:
        if current_note.name == target_name:
            return current_note.guid

def create_note(title, guid, noteStore):
    note = Types.Note()
    note.title = str(today)
    note.content = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml.dtd\">"
    note.content += "<en-note></en-note>"
    note.notebookGuid = target_guid
    note = noteStore.createNote(note)


dev_token = TOKEN
today = datetime.date.today()
client = EvernoteClient(token=dev_token)
noteStore = client.get_note_store()

target_notebook = str(today.year) + '年日記'
target_guid = get_notebook_guid(target_notebook, noteStore)
create_note(today, target_guid, noteStore)
