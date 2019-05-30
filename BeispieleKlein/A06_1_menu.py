i18 = {
    'file': {'en': 'File', 'de': 'Datei', 'fr': 'Fichier', 'it': 'File', }, \
    'new': {'en': 'New', 'de': 'Neu', 'fr': 'Nouveau', 'it': 'Nuovo', } \
}

i18a = {
    'en': {'file': 'File', 'new': 'New', 'open': 'Open', 'save': 'Save', }, \
    'de': {'file': 'Datei', 'new': 'Neu', 'open': 'Öffnen', 'save': 'Speichern', }, \
}

print(i18['file']['de'])
i18['file']['de'] = 'Dateiii'
print(i18['file']['de'])

print(i18a['de']['file'])
i18a['de']['file'] = 'Dateiii'
print(i18a['de']['file'])
