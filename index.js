// Credits to https://til.simonwillison.net/gpt3/chatgpt-applescript, who might credit it to ChatGPT
const Notes = Application("Notes");

Notes.includeStandardAdditions = true;

const notes = Notes.notes();
const noteData = [];

notes.forEach((note) => {
  const noteTitle = note.name();
  const noteBody = note.body();
  noteData.push({
    title: noteTitle,
    body: noteBody,
  });
});

noteData.forEach((data) => {
  fileStr = $.NSString.alloc.initWithUTF8String(data.body);
  fileStr.writeToFileAtomicallyEncodingError(
    `${data.title}-apnotes.html`,
    true,
    $.NSUTF8StringEncoding,
    $()
  );
});
