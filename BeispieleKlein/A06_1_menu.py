otto = {
    'file': {'en': 'File', 'de': 'Datei', 'fr': 'Fichier', 'it': 'File', }, \
    'new': {'en': 'New', 'de': 'Neu', 'fr': 'Nouveau', 'it': 'Nuovo', } \
}

i18a = {
    'en': {'file': 'File', 'new': 'New', 'open': 'Open', 'save': 'Save', }, \
    'de': {'file': 'Datei', 'new': 'Neu', 'open': 'Öffnen', 'save': 'Speichern', }, \
}

print(otto['file']['de'])
otto['file']['de'] = 'Dateiii'
print(otto['file']['de'])

print(i18a['de']['file'])
i18a['de']['file'] = 'Dateiii'
print(i18a['de']['file'])
