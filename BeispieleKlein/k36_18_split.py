import re
logik = """Logik: Die Kunst des Denkens und Schlussfolgerns in 
    strenger Übereinstimmung mit den Beschränkungen und Unfähigkeiten 
    des menschlichen Missverständnisses. Die Grundlage der Logik ist 
    der Syllogismus (logische Schluss), der aus einem Obersatz, einem 
    Untersatz und einer Konklusion (Schlussfolgerung) besteht - somit:
Obersatz: Sechzig Männer können eine Arbeit sechzig mal so schnell machen wie einer.
Untersatz: Ein Mann kann ein Pfostenlock in sechzig Sekunden graben; deswegen
Konklusion: Sechzig Männer können ein Pfostenloch in einer Sekunde graben."""

definitions = re.split('\w+: ',logik)[1:]

print('Defintion von Logik: \n', definitions[0])
print('Beispiel für einen Obersatz: \n', definitions[1])
print('Beispiel für einen Untersatz: \n', definitions[2])
print('Konklusion: \n', definitions[3])
