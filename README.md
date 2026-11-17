**English** · [Français](README.fr.md)

# MIDI Hand

**A glove that plays audio effects.** Holding one of four buttons on the palm turns an effect on in Max/MSP; the arm's tilt and compass heading, read by a BBC micro:bit, steer it.

[![The glove, then the filter, level and auto-pan steered by the arm in the Max/MSP patch (click for the full video)](docs/demo.webp)](https://drive.google.com/file/d/1qyNxkPGdsj8i7iHvZa6W6IYRKT5G1GRB/view)

<details><summary>French version</summary>

[![Le gant, puis le filtre, le volume et le panoramique réglés par le bras dans le patch Max/MSP (cliquer pour la vidéo complète)](docs/demo.fr.webp)](https://drive.google.com/file/d/1QbIa6bsjNl9FtMlIqHvVB8_-le1eRbYG/view)

</details>

*[Full video with sound (1:59)](https://drive.google.com/file/d/1qyNxkPGdsj8i7iHvZa6W6IYRKT5G1GRB/view)*

## Using it

- **A · Filter.** The compass heading sets the low-pass cut-off; a dial in the patch sets the resonance and how much arm tremor is ignored.
- **B · Level.** Raising or lowering the arm raises or lowers the volume.
- **C · Frequency shift.** The same tilt moves the pitch of the patch's oscillator.
- **D · Auto-pan.** Rolling the wrist sets the speed of the left‑right sweep.
- **Combinations.** Button values (1, 2, 6, 10) add up into one MIDI note, so the patch reads any combination on one channel.

## Architecture

<p align="center"><img src="docs/architecture.svg" width="400" alt="MIDI Hand architecture: buttons and sensors on the micro:bit, a MicroPython script sends MIDI over a MIDI-USB cable, the Max/MSP patch applies four effects to a sample or an oscillator"></p>

<details><summary>French version</summary>

<p align="center"><img src="docs/architecture.fr.svg" width="400" alt="Architecture de MIDI Hand : boutons et capteurs sur la micro:bit, un script MicroPython envoie du MIDI par un câble MIDI-USB, le patch Max/MSP applique quatre effets à un extrait ou à un oscillateur"></p>

</details>

## Status

- **Context.** *Interfacing for Audio and Music* module, MSc Audio and Music Technology, University of York, 2021; not developed since.
- **Hardware.** BBC micro:bit on a prototyping board, 4 buttons, potentiometer, battery pack, glove, MIDI‑USB cable.
- **Known gap.** The script computes the compass heading re-centred by the potentiometer but no longer sends it; the patch steers the filter only from that value (CC 24), so with this script the filter does not follow the compass. An earlier version of the script (March 2021) sent it.

---

**Anthony Hunt** · [ingevision.cloud](https://ingevision.cloud/?lang=en&p=midi-hand) · [LinkedIn](https://www.linkedin.com/in/anthony-hunt-3948a9196) · [GitHub](https://github.com/anthohunt)
