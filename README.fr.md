[English](README.md) · **Français**

# MIDI Hand

**Un gant qui joue des effets audio.** Maintenir l'un des quatre boutons de la paume active un effet dans Max/MSP ; l'inclinaison du bras et le cap de la boussole, lus par une carte BBC micro:bit, le règlent.

[![Le gant, puis le filtre, le volume et le panoramique réglés par le bras dans le patch Max/MSP (cliquer pour la vidéo complète)](docs/demo.gif)](https://drive.google.com/file/d/1qyNxkPGdsj8i7iHvZa6W6IYRKT5G1GRB/view)

*[Vidéo complète avec le son (1 min 59)](https://drive.google.com/file/d/1qyNxkPGdsj8i7iHvZa6W6IYRKT5G1GRB/view)*

## Utilisation

- **A · Filtre.** Le cap de la boussole règle la fréquence de coupure du passe-bas ; un bouton rotatif du patch règle la résonance et la part de tremblement du bras ignorée.
- **B · Volume.** Lever ou baisser le bras monte ou baisse le volume.
- **C · Décalage de fréquence.** La même inclinaison change la hauteur de l'oscillateur du patch.
- **D · Panoramique auto.** Tourner le poignet règle la vitesse du balayage gauche‑droite.
- **Combinaisons.** Les valeurs des boutons (1, 2, 6, 10) s'additionnent en une seule note MIDI : le patch lit toute combinaison sur un seul canal.

## Architecture

<p align="center"><img src="docs/architecture.svg" width="400" alt="Architecture de MIDI Hand : boutons et capteurs sur la micro:bit, un script MicroPython envoie du MIDI par un câble MIDI-USB, le patch Max/MSP applique quatre effets à un extrait ou à un oscillateur"></p>

## État

- **Contexte.** Module *Interfacing for Audio and Music*, MSc Audio and Music Technology, université de York, 2021 ; plus développé depuis.
- **Matériel.** Carte BBC micro:bit sur carte de prototypage, 4 boutons, potentiomètre, piles, gant, câble MIDI‑USB.
- **Écart connu.** Le script calcule le cap recentré par le potentiomètre mais ne l'envoie plus ; le patch ne règle le filtre que par cette valeur (CC 24) : avec ce script, le filtre ne suit pas la boussole. Une version antérieure du script (mars 2021) l'envoyait.

---

**Anthony Hunt** · [ingevision.cloud](https://ingevision.cloud/?p=midi-hand) · [LinkedIn](https://www.linkedin.com/in/anthony-hunt-3948a9196) · [GitHub](https://github.com/anthohunt)
