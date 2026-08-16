#!/usr/bin/env python3
"""
RED SIGNAL - Detailed prompt generator for film_parts/ and posts/
Produces book-faithful, much-more-detailed production prompts + social posts.
Source of truth: act1.txt and act2.txt (extracted from the manuscript PDFs).
"""

from pathlib import Path
from datetime import date, timedelta
import calendar

ROOT = Path("C:/Users/USER/Desktop/Projects/RED SIGNAL")
STYLE = "Cinematic sci-fi thriller, film grain, desaturated color grade with red accents, moody atmospheric lighting."

# ---------------------------------------------------------------------------
# SHARED CHARACTER BLOCKS (exact, book-faithful, reference-mapped)
# ---------------------------------------------------------------------------
CHAR = {
    "lyra": ("Front-facing portrait: Lyra Vex, mid-20s, lean athletic build, sharp angular face with strong "
             "jawline, **intense eyes with wide/pupil-dilated pupils** (a recurring tell), short dark hair "
             "cropped practical and slightly messy, pale skin threaded with fine scars, wearing a worn "
             "dark grey tactical jacket (her coat) over a dark shirt, dark combat pants, heavy-duty muddy "
             "boots. Key markers: faint Council-Red-Signal gen-line tag on her back just below the left "
             "shoulder blade, a microdrive concealed beneath her collarbone, nosebleeds when phasing."
             " Ref: references/characters/lyra_vex/lyra_front.jpg"),

    "lyra_fullbody": ("Full-body reference pose, neutral stance: Lyra Vex mid-20s, lean athletic, sharp angular "
                      "face, short dark hair, pale skin, worn dark grey tactical jacket over dark shirt, dark "
                      "combat pants, heavy-duty muddy boots, coat slightly too big. Ref: "
                      "references/characters/lyra_vex/lyra_fullbody.jpg"),

    "josie": ("Profile/mid-shot: Josie Kael, young (early 20s), softer features, light stubble, half-retractable "
              "combat helmet, warm brown eyes that read caution-laced-curiosity not suspicion. Wears Order "
              "field-grey uniform with dark shoulder rig, weapon held low and nonthreatening. "
              "Ref: references/characters/josie_kael/josie_34profile.jpg"),

    "wren": ("Medium shot: Wren Avo, late 20s/early 30s, tall and lean, sharp cheekbones, dark hair in a tight "
              "braid, **visor that swallows her eyes** (only the curve visible). Wears Order black-armor "
              "coat, arms perpetually crossed, permanent skeptical set to her mouth. "
              "Ref: references/characters/wren_avo/Wren_front.jpg"),

    "tomas": ("3/4 shot: Tomas Vale, early 30s, clean-shaven, dark disheveled hair, wire-rim safety glasses "
              "perched low on a narrow nose, hands always moving over controls. Tired but observant eyes, "
              "tech-blue technician coat with cable pouch, carries a diagnostic pad. Ref: "
              "references/characters/tomas_vale/TOMAS_front.jpg"),

    "kael": ("Commander Ivar Kael: late 50s, broad-shouldered 'wall' build, graying beard, rigid posture, cold "
              "assessing steel-grey eyes, wire-rim glasses. Wears Order dress-uniform with gold-thread rank "
              "braiding over a high collar. Ref: references/characters/ivar_kael/Ivar_front.jpg"),

    "sayen": ("Tight mid-shot: Sayen Dray, 30s-40s, clean-cut, unreadable half-smile, dark coat, always arms "
              "loosely folded or fingers drumming a relay spike. Eyes sharp, watchful, one step ahead. "
              "Ref: references/characters/sayen_dray/SAREN_front.jpg"),

    "quill": ("Close-up: Dr. Malen Quill, late 40s, silver hair combed back with precise indifference, pale "
              "dusty eyes behind rimless glasses, thin bloodless lips in a thin smile. Wears a white lab coat "
              "over slate-gray Council-regulation shirt, thin gloves tucked behind his back. Ref: "
              "references/characters/malen_quill/Malen_front.jpg"),

    "holt": ("Wide authority shot: Director Saren Holt, 50s, severe platinum-blonde crew cut, high cheekbones, "
              "cold blue eyes, angular jaw. Wears a flowing charcoal Council coat with subtle red sigil embroidery. "
              "Posture regal and composed. Lighting: cold blue. Ref: references/characters/council/RYNN_front.jpg"),

    "rynn": ("Tight portrait: Envoy Cassel Rynn, 40s, sharp silver-streaked hair, tailored navy-and-white "
              "Council civilian suit, smooth patter, rehearsed sincerity. Smirks like he already owns the room. "
              "Ref: references/characters/council/RYNN_front.jpg"),
}

# ---------------------------------------------------------------------------
# FILM PARTS (22) - book-faithful, far more detailed
# ---------------------------------------------------------------------------
FILM_PARTS = [
    {
        "n": 1, "title": "PROLOGUE", "subtitle": "The Fire Beneath The Skin",
        "chapter": "PROLOGUE",
        "shots": [
            "Crane wide pull-in: hidden bunker carved into a collapsed border-sector ruin, red emergency "
            "lights pulsing across sterile corrugated walls, gas vents hissing thick white smoke, the low "
            "hum of power deep beneath the grated floor. Ash-like particles drift through the stale air.",
            "Handheld close on a flickering terminal: greenish CRT text reading 'SIGMA: HANDOFF' glitches and "
            "fades with a high-pitched whine.",
            "Over-the-shoulder tight: Lyra's gloved hand slipping a microdrive beneath the seam of her jacket, "
            "pressing it flat against her collarbone — the ghost imprint of a Council identifier just visible.",
            "Slow push toward her silhouette: Lyra Vex, back turned, short dark hair, worn grey coat, "
            "shoulders squared as she steps from the bunker into swirling smoke. The glow of the dying "
            "terminal catches the edge of her jaw.",
        ],
        "audio": "Hiss of gas vents, distant low-frequency hum, a single dying electrical whine, faint "
                 "distant siren, the whisper of ash-rain and fabric as she moves.",
        "line": "'I'll be waiting for the signal.'",
        "note": "PROLOGUE establishes the lie she lives inside — the rebellion, the mission, the self. Her face "
                "must read resolve, not fear. This is the last moment before the signal calls her back. "
                "Light ONLY from internal red emergency strips — no external sun/warmth, ever."
    },
    {
        "n": 2, "title": "THE RUINS", "subtitle": "Extraction Run",
        "chapter": "CHAPTER ONE - The Extraction",
        "shots": [
            "Establishing extreme wide drone tilt: skeleton skyline of shattered towers like broken teeth, "
            "cracked windows devoured by fire, cold ash-rain falling like grey snow. No sun — only the orange "
            "glow of distant blaze and red emergency strobes.",
            "Handheld over-shoulder: Lyra crouched under the half-collapsed balcony of an abandoned shop, "
            "breath ghosting white in the dark, hand pressed to a fresh bruise beneath her ribs — a gift from "
            "the jump during the last sweep. Her coat is soaked, boots filled with grime and oil.",
            "POV tight: Lyra's eyes snapping up at a surveillance drone — dim red scanning cone — as it "
            "twitches, its light sputters, sparks rain from its core, and it drops like a stone, smashing into "
            "concrete in a hiss of steam and fried circuitry.",
            "Medium two-shot: her fingers tighten around the drive's concealment as four Order-armored shadows "
            "step from the mist, sniper's laser dot crawling near her chest.",
        ],
        "audio": "Ash-rain pattering on broken concrete, distant fires crackling, the whine of the dying drone, "
                 "boots crunching debris, a sharp crack as a sniper round hits metal, ragged breath.",
        "line": "'I escaped. I have proof of what they're doing in the western camps. Please. If you kill me, "
              "you'll never see it.'",
        "note": "World rules — no sun, no warmth, only red. Show she's hurt (rib bruise) and hiding it. The "
                "drone death is the first wrong note — off-tune, like a broken chord. Josie lowers his rifle "
                "(the first 'soft' thing she meets); Wren stays menace."
    },
    {
        "n": 3, "title": "FIRST CONTACT", "subtitle": "Josie's Patrol",
        "chapter": "CHAPTER ONE (cont.)",
        "shots": [
            "Low Dutch angle wide: four black-armored Order silhouettes materialize from the alley mist, "
            "moving with military precision in the red-gloom. One drops to a crouch, rifle snapped to target.",
            "Close on Wren: visor-swallowed eyes, jaw set — 'Don't move!' crisp, weapon steady.",
            "Medium: Josie stepping up — softer features beneath half-retracted helmet, weapon held low and "
            "steady (non-threatening). His gaze is caution-laced curiosity, not suspicion.",
            "Reaction close: Lyra's fingers tightening on her coat, the drive pressing against her collarbone, "
            "as she answers, voice even but edged.",
            "Handheld crash-cut: Wren yanks her down as a sniper round screams in, metal shrieking, they sprint "
            "through half-flooded streets, boots slapping murky water, rain stinging faces.",
            "Final: inside the evac transport, rain streaking the glass like static, Lyra staring blank ahead, "
            "muscles coiled, the drive concealed but humming against her skin.",
        ],
        "audio": "Rain on metal and concrete, radio chatter 'Extraction point compromised. Detour to fallback "
                 "route Theta-Nine.', rifle bolt click, distant sirens, heavy breathing.",
        "line": "Josie: 'We're not going to kill you.' / Wren: 'Yet.'",
        "note": "The first soft hand — Josie lowers his rifle when she says she's unarmed. The recognition "
                "flicker: her fingers brush his wrist en route and she feels 'something sharp... recognition, "
                "not fear.' Seed the twin pulls: Order safety vs. the signal calling her back."
    },
    {
        "n": 4, "title": "ARRIVAL", "subtitle": "The Order Base",
        "chapter": "CHAPTER TWO - Entry Point",
        "shots": [
            "Wide establishing: mountain-belly facility set into rock, concrete bones anchored against "
            "reinforced steel, hidden from sky-scan. Stark tubular lighting, faint rust stains on bulkheads.",
            "Steam-medium: Lyra stepping through the decontamination chamber — a hiss of hot steam washes "
            "over her, droplets on her dark hair. Josie behind, hands at sides, helmet clipped to belt. "
            "Wren close by, arms crossed, mouth drawn.",
            "Dolly push along corridors: reinforced steel walls, biometric-sealed doors, faded warning signs "
            "('BIOHAZARD', 'CRYPTO LOCKDOWN'). The red-tinged glow from strips is the only warmth.",
            "Close on Lyra's face as she passes a doorway — a micro-twitch of recognition she blinks away. "
            "The spacing of ceiling panels, the door-marker font — she's seen them.",
            "Wide: the command room — warmer lighting, a wall of live surveillance feeds, a desk cluttered "
            "with handwritten notes. Commander Kael stands near the center, arms behind back.",
        ],
        "audio": "Decon steam hiss, recycled-air fans, hydraulic door seal, boot clicks on grated metal, "
                 "low feed-hum from the surveillance wall.",
        "line": "Wren: 'This is a temporary access zone. You'll be processed, screened, and cleared — or you won't. "
              "Don't wander. Don't lie. Don't touch anything you didn't bring with you.' / "
              "Lyra: 'Sounds cozy.'",
        "note": "The base has a pulse beneath the hum — it watches. Josie offers a tired protective shoulder, "
                "Wren stays blade. Kael is built like a wall. The design twitches trigger something buried; "
                "she rationalizes it as déjà vu. This is the first place her false memories meet real architecture."
    },
    {
        "n": 5, "title": "THE ASSESSMENT", "subtitle": "Kael's Desk",
        "chapter": "CHAPTER TWO (cont.)",
        "shots": [
            "Over-shoulder of Kael at his desk: cold steel table, a single microdrive centered like evidence, "
            "his weathered hands steepled. The wall of feeds behind shows her movement, red-tagged.",
            "Medium two-shot: Kael's steel-grey eyes boring into hers, face a mask of 'assessing predator'.",
            "Close: the technician sliding the drive into a secured port — the screen lights with a silent scan.",
            "Two-shot: Kael and Lyra across the table — her hands visible, relaxed (too relaxed), her answer "
            "low and steady.",
            "Cutaway detail: the word 'SIGMA' glowing faintly on a hidden console label behind her chair.",
        ],
        "audio": "Printer whir, quiet keyboard taps, the low electrical buzz of the feed-wall, the pneumatic "
                 "thunk as the drive locks into port.",
        "line": "Kael: 'You're either very brave... or very stupid.' / "
              "Lyra: 'I'm alive. Which is more than most people can say after crossing Council lines.' / "
              "Kael: 'Sigma Cell was reported destroyed two weeks ago during an aerial sweep of Sector Five. "
              "You're the only name we've heard since.'",
        "note": "Kael the wall. The drive 'checks out — encrypted. Not booby-trapped' — but too clean. He offers "
                "the Sigma Cell death line as a live test of her story. Two-day evaluation, surveillance access "
                "restricted — but the cameras stay. The hook that snags: she knows things she shouldn't — and "
                "Kael knows he knows it."
    },
    {
        "n": 6, "title": "FIRST NIGHT", "subtitle": "The Dorm",
        "chapter": "CHAPTER FOUR / CHAPTER FIVE - Quiet Rooms",
        "shots": [
            "Wide establishing: the dorm — concrete platform bed, steel sink, a single camera dom in the "
            "ceiling corner, motion-triggered lights that are slightly too white. Smells of ozone and "
            "antiseptic. No windows.",
            "Mirror-close: Lyra splashing cold water on her face — her reflection stares back, then for one "
            "beat the glass-face is frozen, eyes wide, before snapping back into sync like a buffering glitch.",
            "Tracking: her fingers tracing the room's edge — narrow bunk, sealed locker, wall console locked "
            "to public records. Camera above the door small but unmistakable.",
            "Mid-shot: Lyra studying the facility map on her datapad — she zooms a Sublevel-3 storage schematic, "
            "the support-column pattern, the vent placement — she KNOWS this layout. 'In a memory she "
            "couldn't place.'",
            "Low angle pull: she pads down a dim corridor, past a door marked 'OLD SECTOR: AUXILIARY — "
            "INACTIVE', no lock, hissing open at her touch — revealing a dust-thick room with one familiar chair.",
        ],
        "audio": "Motion-light click-hum, filtered air circulation, water running, her own breath, the soft "
                 "whirr of the camera dom. Almost nothing — the room watches quietly.",
        "line": "'Asset Vex, hold still. Red Signal active. Override engaged.' (voice whispered from inside her "
              "own head). / Door shut with a hiss.",
        "note": "First real crack. The mirror glitch, the layout recognition, the chair in the inactive sector — "
                "all of it memory without a moment. The voice is the first direct leak of the conditioning. "
                "Too-white lights, camera always watching, a room that feels less like acceptance than waiting."
    },
    {
        "n": 7, "title": "THE TRAINING DECK", "subtitle": "Shadow Run",
        "chapter": "CHAPTER SIX - The Test Run",
        "shots": [
            "Wide crane: the training deck — foam-padded obstacles, burst-round targets, sensor mines "
            "spaced across concrete, artificial light harsh overhead. Wren checks pulse-rifle scope, "
            "Josie adjusts gloves, Lyra in a borrowed vest.",
            "Action run (steady-cam, smooth): Lyra flows between obstacles like a shadow — smooth, fast, "
            "automatic. Targets pop: Council soldier projections, drone silhouettes, civilian no-shoots. "
            "Each burst a controlled tap.",
            "Insert POV: her eyes pivoting to anticipate a pop-up drone at 3:12 — she sees it before it rises. "
            "Muscle memory that outruns sight.",
            "Split screen: the biometric readouts — heart 89, flat, no spike even as a flashbang proxy "
            "discharges ten feet away. 'Even when the flashbang proxy detonated ten feet away...'",
            "Close: Wren's hard read — 'That was... cute.' Josie's half-impressed 'How the hell did you—?' "
            "then Wren stalking off.",
            "Cutaway: Tomas in the control hub, rewinding the footage three times, face going pale.",
        ],
        "audio": "PA buzzer 'Begin simulation in five', burst-round report, sensor-mine beep, footfalls on "
                 "foam padding, the electronic crack of the flashbang, the flat whine of readouts.",
        "line": "Lyra: 'Muscle memory.' / Josie: 'From where? Your fake Rebellion?'",
        "note": "She's too good, too smooth — reflexes beyond experience, biometrics unnaturally flat (89bpm). "
                "The simulation is supposed to test her — it only proves she's not surprised by anything in it. "
                "Tomas sees it at a glance: 'Pattern matches conditioning protocol alpha-variant.'"
    },
    {
        "n": 8, "title": "THE ANOMALY", "subtitle": "Tomas' First Look",
        "chapter": "CHAPTER THREE / CHAPTER SEVEN - The Debrief / Fractured Codes",
        "shots": [
            "Wide: the comms archive — three monitors glowing, decryption crawl of the microdrive, "
            "Tomas's silhouette framed by blue light. 'Council formatting with Order-style redundancies. "
            "Weird mix.'",
            "Close: a folder that blinks and collapses — 'RED SIGNAL - VEX/DELTA-EXTRACT - LEVEL 2 "
            "CONDITIONED'. Tomas freezes.",
            "Medium: Room Seven — two chairs, no monitors. Lyra across from Tomas Vale (early 30s, "
            "disheveled, observant tired eyes, safety-glass perched).",
            "Two-shot: Tomas tilts his head 'like pixels that twitch when they lie.'",
            "Over-shoulder: Lyra's intake — 'flatline adrenaline during drone fire,' neural map, biometrics. "
            "Tomas's private note: 'She doesn't know.'",
        ],
        "audio": "Keyboard clatter, monitor fan-hum, the quiet chirp of file open/close, room silence, "
                 "Tomas's pen on paper.",
        "line": "Tomas: 'Keep thinking about that phrase.' / Lyra: 'A room with no walls. A voice that doesn't "
              "have a face. The phrase Red Signal repeating in my head, but I don't know why.'",
        "note": "The first real read on her. Tomas spots the impossible: flatline under fire, the 'weird mix' "
                "of architectures, and that collapsing folder whispering its real label. LEVEL 2 CONDITIONED "
                "= raw memory repatterning / rebellion simulation. He logs 'She doesn't know' — the moment "
                "he decides not to tell her."
    },
    {
        "n": 9, "title": "THE NIGHTMARE", "subtitle": "Sleepwalking",
        "chapter": "CHAPTER NINE - Trigger Response",
        "shots": [
            "Soft white dream-light: the sterile white room, smooth walls, a reclined chair. A man in "
            "slate-gray Council fatigues, sleeves rolled, face blurred at the edges — adjusting something "
            "behind her head, checking vitals.",
            "Extreme close: the insignia on his collar — three broken red circles. 'Lyra. Focus.'",
            "Over-shoulder: 'Tell me what you remember about the breach.' / Her own voice, flat, pre-recorded "
            "but answering: 'I didn't breach. I was sent.'",
            "SMASH CUT to cold hallway: Lyra standing barefoot, hand pressed to the wall, corridor dim, "
            "auxiliary lights pulsing. She has no memory of walking there.",
            "Tracking pull-back: Josie finding her, voice a signal flare. He wraps his jacket around her "
            "shoulders, studies her face in the dim.",
            "Control room inset: Tomas at a console, Zone-5 readouts. 'Dark.' 'Someone cut the feed — "
            "from inside.'",
        ],
        "audio": "Muffled underwater voices (dream), the flat electronic chirp of monitors, an abrupt "
                 "silence, fluorescent hum, Josie's breath, Tomas's murmured 'Someone is protecting her... "
                 "or using her.'",
        "line": "Doctor: 'You won't remember me. But I'll be watching.' / Josie: 'Did they push too hard?'",
        "note": "Sleepwalking is the backdoor — she leaves her room and doesn't remember, her body obeying "
                "pre-programmed paths through pre-wired blind spots. The feed blackout is her own doing "
                "(Internal Failover Trigger). Josie is the soft hand that finds her; Tomas is the first to read "
                "the truth: she walked the halls like 'someone who's trained here before.'"
    },
    {
        "n": 10, "title": "THE QUESTION", "subtitle": "Interrogation",
        "chapter": "CHAPTER FOURTEEN - Skin Memory (flashback reveal)",
        "shots": [
            "Close on the dorm mirror: morning dim, Lyra's reflection pale. Josie just inside the door, "
            "tray of toast and warm water — no soldiers, no doctors, just Josie.",
            "Medium: Josie shifts the blanket, her shirt rides up — reveal of the faint, chemical-washed mark "
            "on her spine, just below the left shoulder blade: an old Red-Signal identifier, Series code. "
            "His fingers freeze. 'It's an old Council gen-line tag.'",
            "Tight two-shot: Lyra recoiling — 'I didn't put it there. I didn't choose any of this.' Her voice "
            "raw, sudden. Tears not far.",
            "Intercut FLASHBACK (sharp, clinical white-blue glauze): the white Council room, a younger Lyra "
            "strapped in, a clean-handed doctor (Quill) planting the detention-camp lie: 'Your parents died "
            "in the riot. The Council tried to cover it up. That's why you joined the Rebellion.' Each "
            "sentence clicks — 'IMPLANT STABLE. SIGNAL DORMANT.'",
            "Return: Josie, quiet — 'You're not fake.' / Lyra, crumbling — 'I remember a detention camp... "
            "but maybe I just think I do. Maybe it's fake.'",
        ],
        "audio": "Drip of tap, toast wrapper crinkle, the flat electronic 'click' of each implant cue, "
                 "Josie's steady breathing, Lyra's choked whisper, bathroom ventilation hum.",
        "line": "Josie: 'What is this?' / Lyra: 'I didn't put it there.' / Implant voice: 'Your parents died "
              "in the riot. That's why you joined the Rebellion.'",
        "note": "The mark on her back is physical proof she was branded before she ever crossed a border. "
                "The flashback implant (Ch 14) proves her core identity is constructed. Josie becomes the "
                "first person she trusts with it. The blood of the lie is warm; the truth cuts deeper than any "
                "blade. Camera stays tight on skin, on hands, on eyes that finally understand they're looking "
                "at a painting, not a person."
    },
    {
        "n": 11, "title": "THE KINDNESS", "subtitle": "The Jacket",
        "chapter": "CHAPTER THIRTEEN - Dormant",
        "shots": [
            "Dusk exterior: Lyra on the observation deck edge, wind whipping her coat, the Order compound "
            "spreading below in red-gloom. She's sketching escape routes on a datapad — choke points, relay "
            "points, blind spots — calculating how to disappear.",
            "Close: her finger tracing her temple — the pressure's back, worse. Memories expanding too fast "
            "for her skull to contain.",
            "Medium: Josie finding her barefoot in the west-corridor hall, offering his jacket without a word. "
            "Silent watch. 'She was out cold... barefoot. You think that's strategic?'",
            "Two-shot low: Josie: 'If I stay, I'm the fuse. If I leave, I light it anyway.' Lyra, raw: "
            "'I don't know what I am anymore.'",
        ],
        "audio": "Wind through the valley, ash-rain on concrete, her pen scratching the datapad, the soft "
                 "click of a jacket zipper, distant compound hum.",
        "line": "Josie: 'If I stay, I'm the fuse. If I leave, I light it anyway.' / "
              "Lyra: 'What if it's all of us?'",
        "note": "The kindest moment: Josie offers his jacket not because she's cold but because she's come "
                "undone. This isn't safety — it's a choice. The jacket becomes the first real anchor. The "
                "camera should breathe: handheld on the wind, locked-off on the two of them talking in the "
                "half-light, never letting the red of the compound intrude. The lie is that she's a weapon; "
                "the kindness is that Josie insists she's still human. That's the fight worth filming."
    },
    {
        "n": 12, "title": "THE FAILSAFE", "subtitle": "Chip Glow",
        "chapter": "CHAPTER FIFTEEN - Archive C (and preview)",
        "shots": [
            "Dust-fall wide: the Archive level — steel shelves layered in dust like ash, unopened crates, "
            "flickering motion-strips. 'A forgotten wing of forgotten files.'",
            "Medium: Kael's file glowing on the holo — surveillance still of a younger Lyra strapped to the "
            "white chair, electrodes at temples. 'Project Echo.'",
            "Close: the black microdrive on the console table — the one Josie recovered from her medkit, "
            "warm, pulsing faintly with a green glyph under her fingertips.",
            "Insertion: Lyra's POV as the drive sparks to life — glyphs crawling across the display, "
            "Council partition tags cracking open. 'Level 2 Conditioned.'",
            "Reaction extreme close: Lyra's pupils flickering — 'You were mine.' / a whisper in the static.",
            "Overhead crane pull-back: the archive's glass walls, the red emergency wash, Wren watching "
            "from the shadows.",
        ],
        "audio": "Dust settling, the low electronics whine of the drive, a rising digital chirp as glyphs "
                 "unfurl, Lyra's breath catching, Wren's muted footfall.",
        "line": "Drive voice: 'Lyra... this is Ion. You were never meant to question. Only to open the door.'",
        "note": "THE FAILSAFE is not a chip — it's a person. Sayen has been the handler all along, and the "
                "Archive C reveal proves the Order knew. Tomas now holds the truth he can't unsee: six Echo "
                "subjects, one survives, one was lost (Echo-One). The chip is warm because it recognizes her. "
                "Light it from inside her palm; make the green glyph the only thing that moves."
    },
    {
        "n": 13, "title": "THE ARCHIVE", "subtitle": "Archive C",
        "chapter": "CHAPTER FIFTEEN - Archive C",
        "shots": [
            "Corridor low angle: 'Archive C — Access Level: AUTHORIZED' the door rumbles open, stale air "
            "rushes out, dust motes in the red-gloom.",
            "Wide interior: Kael and Tomas in a cathedral of dead files, rotating holo of Lyra's biometric "
            "fluctuations pulsing above the table in muted red waves.",
            "Close on holo: 'Project Echo — six subjects. The others failed. Minds fractured. Bodies gave out.' "
            "Kael's hands are tired holding the past.",
            "Medium: Kael turning a photo of young Lyra in the white chair — electrodes at temples. 'She was "
            "engineered for this. Memory scaffolding, behavioral masking, cognitive dampeners.'",
            "Over-shoulder: Dr. Quill's waveform — 'a red loop undulating' — 'Memory recall index. Growing "
            "Erratic.' Tomas's note 'FLAGGED: CONDITIONAL STABILITY - INCONCLUSIVE'.",
        ],
        "audio": "Vault door grinding, paper-rustle of old files, the soft pulse of the holo-display, "
                 "Kael's slow exhale, the distant thrum of the compound.",
        "line": "Kael: 'She was one of six. The others failed. Minds fractured. Bodies gave out.' / "
              "Tomas: 'She's adapting. Maybe even trying to undo what they built.'",
        "note": "Archive C is where the lie collapses. Kael knew. He tells Tomas everything: Project Echo, "
                "the Echo-Class cognitive intervention, the six test subjects. The holo is cold, clinical — "
                "but Kael handles it like a father handling a grave photo. This is the moment the Order stops "
                "reacting and starts choosing. Light the scene in the sickly pulse of the biometric holo; "
                "every face half-lit, every choice heavy. The archive remembers everything; the people inside "
                "it remember nothing they want to."
    },
    {
        "n": 14, "title": "THE TRUTH", "subtitle": "Reading the File",
        "chapter": "CHAPTER TWENTY-ONE - The Ghost Archive",
        "shots": [
            "Tight on Lyra's fingers: a hidden panel behind the east comms wing pries open — 'Welcome back, "
            "Lyra Vex. Archive access: Echo-tier clearance confirmed.' The screen knows her name.",
            "Medium: the folder 'ECHO UNIT LOGS - DEPLOYMENT REELS 08-10' pulsing like a heartbeat. "
            "Operation: Gatefall Ridge. Operation: Blue Wane. Operation: Dustlight.",
            "POV scroll: mission names with their true labels — 'Simulated Field Engagement - Asset Training', "
            "'Supervised Response Conditioning', 'Council Construct - Observational Theatre Approved'.",
            "Close: the footage — younger Lyra coordinating with 'Ferris', 'Kamel', 'Olsen' in a sealed "
            "training room. Their body language too clean, too rehearsed. Not war-worn.",
            "Reaction: the status readouts — FERRIS: DECEASED 'Post-trial cleansing. Memory loop expired.' / "
            "KAMEL: UNLOCATED 'Transfer terminated.' / OLSEN: INACTIVE 'Deprogrammed.'",
            "Slow zoom: Lyra's face as she reads her own file — 'Primary Role: Constructed Defector. "
            "Override Status: Active. Command Code: Red Signal - Phase II. Await Initiation.'",
            "Final frame: Sayen emerging from the dark, arms folded — 'You found it.'",
        ],
        "audio": "Dust crackle, terminal boot whine, the silent replay of surveillance footage, a page "
                 "turning, Lyra's breath hitching, Sayen's footfall.",
        "line": "File: 'Asset: LYRA VEX. Deployment: ORDER INFILTRATION. Primary Role: Constructed Defector. "
              "Command Code: Red Signal - Phase II. Await Initiation.' / Sayen: 'You found it.'",
        "note": "THE TRUTH is data, and it kills. The Ghost Archive proves her rebellion was a film set. "
                "Every friend, every loss, every night of passion was scripted and supervised by Dr. Quill. "
                "The statuses read like execution warrants disguised as performance review. Sayen's arrival "
                "at the end recontextualizes everything: he didn't find her by chance — he delivered her. "
                "The screen should bleed red as the truth loads; Lyra should look like she's being flayed "
                "by the very thing that was supposed to save her. Keep the glyphs visible, the labels brutal, "
                "and the final face-reveal of Sayen in the shadows — he's been the handler inside the Order."
    },
    {
        "n": 15, "title": "THE BREAK", "subtitle": "Collapse",
        "chapter": "CHAPTER TWENTY-TWO - Proxy War",
        "shots": [
            "Handheld: Lyra stumbling through dim corridors, legs on reflex, brain like static — fake "
            "missions, lies parading as memory, Sayen's voice: 'You were meant to return.'",
            "Close: her boot crushing the 'Trust none. Don't drink the images. Freedom has no sponsor.' "
            "graffiti of the old pre-Council rebel zone.",
            "Medium: the infirmary cot — she's bandaged, pale, eyes 'wrong, like someone else borrowed her "
            "skin for a while.' Tomas holding her shoulders, his voice 'breaking through static.'",
            "Two-shot: Wren sliding the neural strip across — 'It spiked. Massive stress response. But no "
            "external trigger.'",
            "Slow push: the med-analysis hologram — 'Engineered fear. The kind they used to break test "
            "subjects before folding them into deployment roles.'",
        ],
        "audio": "Ash-dust under boots, her ragged breath, the flat electronic whine of the neural strip, "
                 "Tomas's quiet 'You okay?', the hum of medbay machinery.",
        "line": "Wren: 'It wasn't a dream. It was a memory file.' / "
              "Lyra: 'He told me I was ready. And I believed him.' / "
              "Tomas: 'She's not theirs.'",
        "note": "THE BREAK is the collapse of identity in real time. Ch 22 shows her realizing the rebellion "
                "was a simulation; Ch 19 proves the dreams were implanted memory files. The med-bay strip "
                "proves the Council still transmits to her. Camera should be handheld, urgent, slightly "
                "unsteady — she's dissociating as she walks. Let the red glow from the strip be the only "
                "color. Her eyes must look wrong, borrowed. This is the moment she stops pretending the "
                "voices in her head are just dreams."
    },
    {
        "n": 16, "title": "THE RESOLVE",
        "subtitle": "Act 1 Finale | 'I'm not their weapon anymore.'",
        "chapter": "CHAPTER SIXTEEN: Drift Pattern / End of Act 1",
        "shots": [
            "Close on Lyra's palm: she writes Council glyphs — the same shapes from her sleep-script — "
            "onto a torn mission log page, ink blotting through like old bruises.",
            "Over-shoulder: her other hand clutches the microdrive — 'warm. A faint pulse in her fingers.' "
            "A Council-issue black chip, barely thumbnail-sized.",
            "Wide low: her reflection in the data-console glass — double-exposed with the ghost of a "
            "younger Lyra in the white chair, Dr. Quill's silhouette over both.",
            "Extreme close: her voice, raw but steady — 'I'm not their weapon anymore.'",
            "Medium: her thumb smearing fresh blood across the drive's contact points — 'They built me to "
            "begin. I begin instead.'",
            "Pull-back crane: the medbay lights flickering, the red emergency wash, her silhouette "
            "standing over the scorched remains of the chip in a metal cup.",
        ],
        "audio": "Ink scratch on paper, the low electronic whine of the drive, her breath hitching, "
                 "metal sizzling, the soft static of a neural storm, distant compound hum.",
        "line": "Chip voice: 'Lyra. If you're hearing this... it means the drift pattern is holding. "
              "Your host mind remains intact. That's good. You've gone farther than the others.' / "
              "Lyra: 'I'm not their weapon anymore.'",
        "note": "ACT 1 FINALE is the moment she stops resisting the trigger and starts authoring her own. "
                "She has the black chip from her medkit, Josie found it, and she activates it — only to "
                "hear Ion's ghost tell her she's the ignition, not the escapee. Then she speaks in full "
                "Council code — 'Echo vector aligned.' — and collapses with a nosebleed. Resolve means "
                "she chooses her own sentence to finish. Frame it so the glyphs she draws are the only "
                "real color; the rest is red-tinged monochrome. End on her voice carrying past the static."
    },
    {
        "n": 17, "title": "ACT 2", "subtitle": "The Alarm",
        "chapter": "CHAPTER EIGHTEEN - Smoke Between Allies",
        "shots": [
            "Close: Lyra blinking awake on the infirmary cot, dried blood crusted beneath her nostrils. "
            "The surveillance monitor blinks red, then stabilizes — no one is watching.",
            "Mirror-medium: her own reflection — eyes 'looked wrong. Like someone else had borrowed her "
            "skin for a while.' Pupils too wide, color off.",
            "Wide: the corridor outside — Tomas at a terminal, scanning security logs that read 'OFFLINE "
            "for exactly 8 minutes and 17 seconds.' Sayen in frame, arms folded, calm.",
            "Two-shot tension: Tomas, sharp: 'Funny how your breach lines up with the surveillance "
            "blackout.' Sayen, unruffled: 'Coincidence isn't causation, Lieutenant.'",
            "High angle: Wren by the console, chewing her cheek — 'Your breach didn't happen.'",
            "Pull: the observation deck at night, Lyra alone with the neural strip in her palm, finger "
            "tracing its glow. 'Was she still pretending to be a weapon? Or had the pretending long over.'",
        ],
        "audio": "Medbay beep, the static-snarl of a corrupted feed, Tomas's keyboard, the soft whir of the "
                 "monitor, wind in the upper deck, the faint electronic thrum of the strip.",
        "line": "Tomas: 'You vanished without contact. Now Lyra collapses, our systems glitch, and the only "
              "unlogged movement in that timeframe is you.' / Sayen: 'Perhaps you're asking the wrong "
              "questions.'",
        "note": "ACT 2 opens with Lyra's first conscious moment of not-remembering — she wakes to silence, "
                "to a body that moves like borrowed skin, to the knowledge that her 'collapse' was real but "
                "her memory of it is gone. The 8:17 blackout is the first explicit proof someone is "
                "operating time inside her head. The alarm isn't loud — it's quiet, the click of a system "
                "failing while everyone stands around it. Frame her reflection so the camera can't decide "
                "which version of her is real."
    },
    {
        "n": 18, "title": "ACT 2",
        "subtitle": "Josie's Choice | 'I trust you.'",
        "chapter": "CHAPTER TWENTY-TWO - Proxy War / Interlude",
        "shots": [
            "Wide: the Order war-room — oval table, a rotating holo of Lyra's neural imprint, Kael's jaw "
            "like cracked obsidian. Four ranking officers. Maps of Council troop movements bleeding red.",
            "Close: Josie dropping the drive on the table — 'This one was taken two nights ago. Matches "
            "exactly to what she saw in her sleep — frame for frame.'",
            "Medium: Kael studying the hologram, voice flat — 'We didn't intercept her. She was delivered.'",
            "Two-shot: Lyra to Josie — 'You said you believed in what we were doing. Do you still believe in me?'",
            "Extreme close on Josie's eyes — his jaw tight — 'I don't know what you are, Lyra. But I know "
            "what you've done since you got here. You saved people. You told the truth when you didn't "
            "have to.'",
            "Slow push: his hand extending — 'I trust you. Even if I don't fully understand you.'",
            "Counter-shot: Lyra's fingers closing around his — a silent, shaky yes.",
        ],
        "audio": "Holo-whirr, the scrape of a drive on steel, chair legs scraping, the low thrum of war-room "
                 "servers, two heartbeats syncing.",
        "line": "Josie: 'I don't know what you are, Lyra. But I know what you've done since you got here. "
              "You saved people. You told the truth when you didn't have to.'",
        "note": "Josie's choice is the hinge Act 2 turns on. In Ch 22 he's the one who still reaches when "
                "everyone else recoils — 'I trust you, even if I don't fully understand you.' This is the "
                "moment she could be handed back to the Council or claimed by the Order, and she stakes her "
                "place on neither side. The lighting should be the cold war-room wash — practical, unforgiving — "
                "so the only warmth in the frame is Josie's hand. End on the grip of her fingers closing over "
                "his: trust as the last thing the programming can't simulate."
    },
    {
        "n": 19, "title": "ACT 2",
        "subtitle": "Wren's Hunt",
        "chapter": "CHAPTER TWENTY-ONE / Twenty-nine",
        "shots": [
            "Low angle: Wren in the east data-wing, her visor catching the corridor's red emergency strip, "
            "hands a blur over keyboard — 'She's pulling away from their pattern, but not enough.'",
            "Close: her screen splits — Lyra's real baseline (unfiltered cognitive signal) vs. now, "
            "interlaced and shrouded in glyphic interference.",
            "Medium: Wren isolating Sayen's metadata — origin tags reading 'Initiator: Lt. Sayen Dray. "
            "Timestamp adjusted manually. Clearance: Overridden.' Her face darkens.",
            "POV: the planted surveillance clip of Tomas over her sleeping form, neural code on a pad — "
            "fabricated, timestamp wrong by an hour.",
            "Close: Wren's thumb hovering over SEND, then pulling back — 'Your mistake was thinking I "
            "needed to like Tomas to believe him.'",
            "Over-the-shoulder: she spins a fake file with a false confession from Josie into the relay.",
        ],
        "audio": "Keys clicking, data-stream static, the soft whir of the scanner, Wren's breathing — "
                 "controlled, then a beat where it's not.",
        "line": "Wren: 'He planted it so everyone would.' / planted-file: 'He's been with her every step. "
              "When she wandered. When she collapsed. When her signal spiked.'",
        "note": "Wren's hunt is the mirror image of everyone else's — she's hunting the truth but sowing lies "
                "to do it. Ch 21 shows her finding the ghost signatures; Ch 29 shows her turning that skill "
                "against a trap she rigs for Tomas. Her visor is down the whole time, but her eyes do the "
                "real watching. The planted footage should look identical to the real thing until a single "
                "timestamp glitches — that's the detail that saves them. Keep the red strip as the only "
                "constant; every window shows a different version of the same moment."
    },
    {
        "n": 20, "title": "ACT 2",
        "subtitle": "Tomas' Forensics",
        "chapter": "CHAPTER TWENTY / Twenty-one",
        "shots": [
            "Close: Tomas's face, no sleep, terminal blue halo on his skin, layers of telemetry open. "
            "He isolates a low-frequency pulse buried in her fugue-state logs.",
            "Medium: the spike at 1/4 speed — 'Council pattern. Echo-Class Cognitive Intervention Trials.' "
            "The label is a ghost to him.",
            "Wide: Tomas at the archive terminal, entering the hidden neural sequence, narrowing a search "
            "to 15-year visual logs. One file auto-previews — Council-tagged, classified.",
            "POV: the silent training tape — younger Lyra sparring with 'Ferris', exact same angle, same "
            "footwork, same breath pattern her body still knows.",
            "Tight: his hand freezing on the play button — 'Her entire memory... had been recorded. Not "
            "remembered. It was a script.'",
            "Over-shoulder: he spins to Wren, voice raw — 'Someone never left. And whoever they are, they "
            "just cut my access.'",
        ],
        "audio": "Terminal hum and chatter, the whine as he slows the waveform, the static-crackle of the "
                 "found footage, a chair scraping, his voice a ragged whisper.",
        "line": "Tomas: 'We're not just watching her. We're inside her.' / Found file: 'Asset: LYRA VEX. "
              "Override Status: Active. Command Code: Red Signal - Phase II. Await Initiation.'",
        "note": "This is the forensic moment: not theory, not suspicion, but proof. Tomas isolates the "
                "Council carrier pulse from her neural logs and then finds the training footage Ch 20 proves "
                "every move was recorded before she 'remembered' it. The footage should look identical to a "
                "memory until frame-accurate playback reveals the edges are too clean. Frame Tomas as the "
                "classic no-sleep detective, but keep him tender — he's the one who still believes she can "
                "outrun what she was built to be."
    },
    {
        "n": 21, "title": "ACT 2",
        "subtitle": "The Escape",
        "chapter": "CHAPTER THIRTY-FIVE - The Split",
        "shots": [
            "Low: the maintenance tunnel, Lyra's palm pressed to the wall, face set with purpose — "
            "'She wasn't just unraveling. She was authoring.'",
            "Close: the bio-injector in her palm — silver, cold, humming faintly. She reads the label — "
            "'Field-grade neural signature null.'",
            "Medium: her voice, steady — 'I'm not running to any of them. I'm running from all of them.'",
            "Handheld: she slides the injector into her neck — a hydraulic hiss, a wave of numbness, her "
            "biometric signature: NULL — the system's warning light flares once, then dies to static.",
            "High angle tracking: bare feet on cold steel as she palms the exit panel — 'A ghost walking '.",
            "Reverse: behind her, the medbay door opening — Wren's silhouette, arms crossed, 'She's not "
            "rogue. She's waking up.'",
        ],
        "audio": "Tunnel drip, the injector's pneumatic hiss, her breath evening out, the electronic warble "
                 "of a null signature, distant compound thrum, Wren's quiet footfall.",
        "line": "Lyra: 'I'm not running to any of them. I'm running from all of them.'",
        "note": "THE ESCAPE is an act of authorship, not flight. Ch 35 makes her the architect of her own "
                "exit — she takes the field injector Kael's men offered her, blanks her signature so the "
                "Council can't track her, and walks the Order's own tunnels out. She's not defecting to the "
                "Council or begging the Order; she's becoming no one. The injector should glow cold-silver "
                "in her palm, the moment she presses it to her neck should feel like a key turning in a lock "
                "she didn't know existed. End on her bare feet against steel — the first real step into the "
                "person she chooses to be."
    },
    {
        "n": 22, "title": "ACT 2",
        "subtitle": "The Signal | 'Who burns first?'",
        "chapter": "CHAPTER THIRTY-SEVEN - Faultline Ignition",
        "shots": [
            "Wide storm: Zone Thirteen's outer ruins, graffiti on crumbling walls — 'Trust none. Don't drink "
            "the images. Freedom has no sponsor.' Ash drifts through dead air.",
            "Close: Lyra's reflection in shattered control glass — hair tangled, eyes sharper than ever, "
            "human, haunted, FREE.",
            "Medium: her fingers on the field transmitter, voice recorded but raw — 'If you're hearing "
            "this... I was not lost. I was left here.'",
            "POV: the glyph map she etched into the relay bunker wall — 'RS-VEX // PHASE I // OBSERVE', "
            "now overwritten with her own new symbol, no encryption, broadcast on Council relay.",
            "Extreme close: the transmitter clicking as it encrypts her final words, pulses breaking across "
            "unused emergency bands — 'If I light the match... who burns first?'",
            "Pull-back: the Order war room where Holt watches the burst, Quill at his neural map, "
            "Cassel smiling — 'Let her run. Let her crash.'",
            "Final wide: Lyra on the ridge, silhouette against the bruised sky, the red pulse on the "
            "horizon answering her signal.",
        ],
        "audio": "Wind through ruins, ash skittering on stone, the transmitter's electronic chatter, "
                 "her voice cracking, a heartbeat, then a rising electronic swell.",
        "line": "Lyra: 'If I light the match... who burns first?' / Ion (V.O., echoing): 'She was built to "
              "begin. And now she begins.'",
        "note": "THE SIGNAL is the last image of Act 2: the pulse she sent into the dark answered by a "
                "red flare on the horizon. Ch 37 has her recording her final broadcast from the relay tower "
                "and stepping into the frost belt, biometric null, carrying the truth like a lit fuse. The "
                "Order and the Council are both hunting a ghost, but the ghost is the one who just declared "
                "war on both their stories. End with her silhouette and the distant red pulse — the signal "
                "stays on, but now she holds the key. This is not freedom; it is the prelude to choice."
    },
]

# ---------------------------------------------------------------------------
# POSTS (31 days x 3 posts) - much more detailed, book-faithful
# ---------------------------------------------------------------------------
# We keep the existing day-themes, but expand every prompt (image/video) into
# multi-shot, multi-layer detail and weave verified book quotes + beats into captions.

# Shared caption "voice" — a one-line hook line that introduces each post's theme.
# Each post: {"type": "Image"|"Video", "tool":..., "prompt":..., "ref":..., "caption":...}

def image_prompt(detail):
    return f"{detail} {STYLE}"

def video_prompt(detail, audio=""):
    a = f"\nAudio: {audio}" if audio else ""
    return f"{detail} {STYLE}{a}"


POSTS = {
    1: {"theme": "PROLOGUE & REVEAL",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Cinematic title card for 'RED SIGNAL'. A single, slow-pulsing red emergency light in a "
                "black void, thin strands of ash-rain falling through one harsh collimated beam, faint "
                "silhouette of a ruined city skyline (broken towers like teeth) in the deep, smog-choked "
                "background. Bold, blocky, slightly weathered typography reading 'RED SIGNAL' in the centre. "
                "Deep blacks, desaturated blue-grey grade with a red accent glow, film grain, shallow "
                "depth of field."),
             "caption": "A red signal in the dark.\n\nRED SIGNAL — a dystopian sci-fi thriller told in film clips. "
                        "Characters, world, and scenes built for screen.\n\nFollow to see how it unfolds."},
            {"type": "Image", "prompt": image_prompt(
                "Ultra-wide establishing: the hidden bunker carved into the ruins of a collapsed "
                "border-sector transport line, red pulsing emergency strips cutting through thick smoke, "
                "gas vents hissing, a broken terminal reading 'SIGMA: HANDOFF' on the far wall. Lyra Vex — "
                "mid-20s, short dark hair, pale skin, worn grey tactical jacket — adjusting her collar, one "
                "hand concealing a microdrive beneath it. Desaturated grade, deep blacks, red emergency "
                "glow as the only colour, film grain."),
             "caption": "They told her no one escapes the Council.\n\nBut Lyra Vex did. And the drive hidden "
                        "beneath her collarbone is the first lie of a story that was never hers to begin."},
            {"type": "Text-only", "prompt": None, "caption":
                "The signal is a phrase, a glyph, a pulse beneath the skin.\n\n'Asset Vex, hold still. "
                "Red Signal active. Override engaged.'\n\nThis is not a story about what happened. It's "
                "about what was made to feel like it did. Drop a ⚙️ if you're ready to meet the weapon "
                "who doesn't know it's loaded."},
        ]},
    2: {"theme": "THE PROTAGONIST - LYRA",
        "posts": [
            {"type": "Image", "prompt": image_prompt(CHAR["lyra"]),
             "caption": "Meet Lyra Vex.\n\nA trained operative. A flawless soldier. And someone else's weapon — "
                        "she just doesn't know it yet.\n\n'You don't flinch. You don't doubt. That's not instinct. "
                        "That's control.'"},
            {"type": "Image", "prompt": image_prompt(CHAR["lyra_fullbody"]),
             "caption": "Light on gear. Heavy on instinct.\n\nLyra travels light — a runner, not a tank. One "
                        "microdrive hidden under her collar is the most dangerous thing she carries.\n\nShe "
                        "doesn't know what it contains. Yet."},
            {"type": "Text-only", "caption":
                "WHO IS LYRA VEX?\n\nA rebel infiltrator sent to expose the Council?\n\nA programmed asset who "
                "only thinks she is?\n\nAsk her the wrong question and watch her eyes.\n\nCharacter card pinned "
                " — full backstory coming this week."},
        ]},
    3: {"theme": "THE ALLY - JOSIE",
        "posts": [
            {"type": "Image", "prompt": image_prompt(CHAR["josie"]),
             "caption": "First contact.\n\nJosie Kael doesn't raise his rifle first. He watches, listens, and "
                        "lowers the barrel when she says she's unarmed.\n\n'She doesn't look like bait.'"},
            {"type": "Image", "prompt": image_prompt(
                "Action moment: Josie Kael (young, soft features, half-retractable helmet, warm brown "
                "eyes) grabbing Lyra's arm and pulling her down as a sniper round screams past, "
                "sparks striking metal near their feet. Rain-slicked ruined street behind them. Dynamic "
                "angle, film grain."),
             "caption": "A soldier who reads more than stance.\n\nWhen everyone else sees a threat, Josie "
                        "sees hesitation. That single choice — lowering his rifle — is the moment the war "
                        "changes sides."},
            {"type": "Text-only", "caption":
                "They found her bleeding in the ruins.\n\nInstead of cuffing her, Josie handed her his jacket.\n\n"
                "'If I stay, I'm the fuse. If I leave, I light it anyway.'\n\nSome choices don't ask permission."},
        ]},
    4: {"theme": "THE INVESTIGATOR - TOMAS",
        "posts": [
            {"type": "Image", "prompt": image_prompt(CHAR["tomas"]),
             "caption": "Meet Tomas Vale.\n\nHe doesn't trust easily — least of all the stories people tell "
                        "themselves. He trusts scans.\n\n'She didn't tell me anything. Not about the chip.'"},
            {"type": "Image", "prompt": image_prompt(
                "Medium shot: Tomas Vale at a bank of three monitors, blue terminal glow on his pale face, "
                "wire-rim glasses catching the light, dark technician coat, hands flying over keys. "
                "Overlaid data: biometric spikes, neural flatlines, encrypted Council tags. Rain streaks "
                "the small window behind him."),
             "caption": "He rewound her run three times.\n\nHeart rate: 89. No spike. No deviation — even "
                        "when a flashbang detonated ten feet away.\n\n'Pattern matches conditioning protocol "
                        "alpha-variant.'"},
            {"type": "Text-only", "caption":
                "Tomas has seen conditioning before.\n\n'Not all of it. Not the kind built into the bone.'\n\n"
                "He's the first to catch her speaking Council code in her sleep.\n\nAnd the first to decide "
                "not to tell her."},
        ]},
    5: {"theme": "THE MENACE - WREN",
        "posts": [
            {"type": "Image", "prompt": image_prompt(CHAR["wren"]),
             "caption": "Meet Wren Avo.\n\nShe doesn't trust easily — least of all the stories people tell "
                        "themselves. She trusts scans... and her rifle scope.\n\n'She's not just a girl. "
                        "She's a system now.'"},
            {"type": "Image", "prompt": image_prompt(
                "Tight mid-shot: Wren Avo (late 20s, visor swallowing her eyes) crouched in the abandoned "
                "diagnostics lab, fingers ghosting over a keyboard, her breath visible in the cold-air glow. "
                "Behind her, a neural strip reads 'Engineered fear' in red glyphs."),
             "caption": "Wren doesn't plant doubt. She sharpens it.\n\n'The kind they used to break test "
                        "subjects before folding them into deployment roles.'\n\nShe sees the programmed "
                        "terror in Lyra's dreams — and recognizes the hand that planted it."},
            {"type": "Text-only", "caption":
                "Wren doesn't trust easily.\n\n'Your mistake was thinking I needed to like Tomas to believe "
                "him.'\n\nShe builds traps for traitors — including the ones she accidentally trusts.\n\nThis "
                "week: the hunt turns."},
        ]},
    6: {"theme": "THE AUTHORITY - COMMANDER KAEL",
        "posts": [
            {"type": "Image", "prompt": image_prompt(CHAR["kael"]),
             "caption": "Meet Commander Ivar Kael.\n\nA wall of a man — beard grizzled, shoulders broad, "
                        "eyes like cracked obsidian.\n\n'We've been baited before.'"},
            {"type": "Image", "prompt": image_prompt(
                "Wide: Kael in his command-chamber, arms behind back, starlight from the mountain ridge "
                "cutting across his profile. Behind him, a wall of surveillance feeds glows red. The air is "
                "sharp with unspoken decisions."),
             "caption": "He led the Order for thirteen years.\n\n'We don't know what she'll say. And if she "
                        "collapses in public? If the Red Signal activates mid-broadcast?'\n\nKael doesn't react "
                        "to threats — he prices them."},
            {"type": "Text-only", "caption":
                "Kael held a secret.\n\n'Project Echo. Six subjects. The others failed.'\n\nHe buried it before "
                "he told anyone. Some silences are heavier than betrayal.\n\nWhat would you pay to know the "
                "truth about the people you trust?"},
        ]},
    7: {"theme": "THE SHADOWS - DRAY, QUILL & THE COUNCIL",
        "posts": [
            {"type": "Image", "prompt": image_prompt(CHAR["sayen"]),
             "caption": "Meet Sayen Dray.\n\nQuiet. Efficient. Unreadable. Kael's go-to for off-grid "
                        "intelligence.\n\n'If she doesn't return, he'll trigger the final transfer.'"},
            {"type": "Image", "prompt": image_prompt(CHAR["quill"]),
             "caption": "Meet Dr. Malen Quill.\n\nThe architect. The father in the white room. The hand "
                        "that wrote her rebellion.\n\n'You were always meant to escape.'"},
            {"type": "Image", "prompt": image_prompt(CHAR["holt"]),
             "caption": "Meet Director Saren Holt.\n\nHead of Narrative Control. He shapes the world's "
                        "memory — including hers.\n\n'She fractures beautifully. Let her.'"},
        ]},
    8: {"theme": "THE WORLD - COMMAND ROOM",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Wide establishing: the Order command room — wall of live surveillance feeds, a central "
                "holographic table projecting terrain and troop markers, Commander Kael's desk with "
                "hand-written logs. Stark lights, reinforced steel, red emergency wash. Deep blacks, "
                "desaturated grade, film grain."),
             "caption": "The Order's nerve centre.\n\nEvery conversation is recorded. Every hesitation logged. "
                        "Every doubt measured against a standard nobody knows they're held to.\n\nThey watch "
                        "everything. Except the one thing that matters."},
            {"type": "Image", "prompt": image_prompt(
                "Close detail: a holographic display of Lyra's neural imprint rotating mid-air, red waves "
                "pulsing — heart rate, neural index, emotional sync 'unreadable'. Kael's weathered hands "
                "gesturing over the data."),
             "caption": "Her vitals are not a reading. They're a weapon.\n\nHeart rate: erratic.\nNeural "
                        "index: fluctuating between compliance and dissonance.\nEmotional sync: unreadable.\n\n"
                        "'Untraceable. Patternless.'"},
            {"type": "Text-only", "caption":
                "The command room never sleeps.\n\nIts walls are lined with eyes that never blink, and its "
                "tables hold the futures of people who think they're choosing freely.\n\nWhat does it mean "
                "when the watchers are also the watched?\n\n#BehindTheSignal"},
        ]},
    9: {"theme": "THE WORLD - WHITE CHAMBER",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Cinematic wide: sterile white conditioning room — smooth seamless walls, a single reclined "
                "chair with restraint straps and cranial interface ports overhead, soft white LED grid in "
                "the ceiling. A blurred figure (Dr. Quill) leans over a prone Lyra. No shadows — the light "
                "is clean, manufactured, flawless. Deep blacks around the edges, film grain."),
             "caption": "This is where stories are born.\n\n'You're doing beautifully. Now let's go over it "
                        "again — your name, your mission, your reason to hate the Council.'\n\nThe white "
                        "room remembers everything. And Lyra is its favourite student."},
            {"type": "Image", "prompt": image_prompt(
                "Close on the chair's restraint straps and cranial ports, glinting chrome against the "
                "white. A single red glyph flickers in the corner of the ceiling monitor — the first, "
                "faint pulse of 'IMPLANT STABLE. SIGNAL DORMANT.'"),
             "caption": "They didn't chain her.\n\nThey rewired her.\n\n'IMPLANT STABLE. SIGNAL DORMANT.'\n\n"
                        "The machine beneath the skin isn't mechanical. It's belief."},
            {"type": "Text-only", "caption":
                "What if your first memory was a lie?\n\nWhat if the room that raised you was a studio, "
                "and the voice that tucked you in was a technician?\n\n'Time to come in, darling. "
                "Supper's ready.'\n\nThe most dangerous stories are the ones we tell ourselves."},
        ]},
    10: {"theme": "THE WORLD - RUINS & RAIN",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Wide: the post-war ruins at twilight — cracked towers rising like broken teeth, ash-rain "
                "falling like grey snow, distant fires casting orange light. Lyra in the foreground under a "
                "half-collapsed balcony, her silhouette sharp against the glow, one hand on her bruised side. "
                "Deep blacks, red emergency accents, film grain."),
             "caption": "This is where it begins.\n\nRain comes down like ash — cold, scattered, hungry. "
                        "No sun. No warmth. Only the orange of distant fires and the red of forgotten alarms.\n\n"
                        "She carries a drive and a bruise. And a memory that isn't hers."},
            {"type": "Video", "prompt": video_prompt(
                "8-10 second tracking shot through the ruined streets: ash-rain slicking broken concrete, "
                "puddles reflecting red emergency strobes, Lyra's boots splashing through grime, her coat "
                "trailing. A surveillance drone buzzes overhead, then twitches and drops in a shower of sparks.",
                "ash-rain patters, drone whine dying to static, distant fires crackling, heavy breathing."),
             "caption": "Close your eyes.\n\nListen: that's not rain. It's the sound of a world that forgot "
                        "to mourn.\n\nShe runs through it carrying proof — and a feeling she's already been "
                        "in these streets before."},
            {"type": "Text-only", "caption":
                "The ruins don't forgive.\n\nThey remember.\n\nEvery crack in the concrete, every rusted "
                "sign, every shadow that moves when no one walks there — the ruins know her name.\n\nAnd "
                "the ruins were built by the Council.\n\nIs that coincidence... or design?"},
        ]},
    11: {"theme": "THE SIGNAL - RED LIGHT",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Close-up: a single red emergency signal light pulsing on a dark metal wall, its beam "
                "cutting through the dark. The reflection of Lyra's wide eyes in the polished surface, "
                "pupils dilated. Desaturated red-blue grade, deep blacks, film grain."),
             "caption": "It's not a light.\n\nIt's a key.\n\n'Asset Vex, hold still. Red Signal active. "
                        "Override engaged.'"},
            {"type": "Image", "prompt": image_prompt(
                "Extreme close: Lyra's pupils dilating in a dark corridor — the tell. The way her eyes "
                "get too wide, too still, like someone else is looking through them. A faint Council glyph "
                "flickering at the edge of frame."),
             "caption": "Watch her eyes.\n\nWhen the signal hits, she doesn't flinch. She focuses. Becomes "
                        "something smoother, sharper, too ready.\n\n'The phrase Red Signal repeating in my "
                        "head, but I don't know why.'"},
            {"type": "Text-only", "caption":
                "Red means stop.\n\nTo the Council, red means activate.\n\n'Override acknowledged. Delay "
                "protocol.'\n\nOne phrase. One breath. One woman deciding whether to obey.\n\nThe signal "
                "is always on. The question is who's listening."},
        ]},
    12: {"theme": "LYRA - TRAINING DECK",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Wide action: the Order training deck — foam obstacles, burst-round targets, sensor mines "
                "under harsh artificial light. Lyra moving through the course like a shadow, fluid and "
                "silent, a rifle in each hand, targets popping in her periphery. Dynamic angle, film grain."),
             "caption": "She walks through the simulation like she's done it before.\n\nBecause she has.\n\n"
                        "'Muscle memory. From where? Your fake Rebellion?'"},
            {"type": "Image", "prompt": image_prompt(
                "Split frame: Lyra hitting the final beacon, weapon held low, face expressionless, "
                "perfect. On the right, the biometric overlay — heart rate 89, flat, no spike 'even when "
                "the flashbang proxy detonated ten feet away.'"),
             "caption": "89 beats per minute.\n\nNot 130. Not 150.\n\n89.\n\nEven when the flashbang "
                        "detonates ten feet away. Even when the targets scream back. Her body doesn't "
                        "register the drill as danger.\n\nBecause it was never a drill."},
            {"type": "Text-only", "caption":
                "Tomas rewound the footage three times.\n\n'Pattern matches conditioning protocol "
                "alpha-variant. Suggest further behavioral testing under emotional duress.'\n\nShe wasn't "
                "built for the Order.\n\nShe was built for the Council.\n\nAnd the deck? It's not new to "
                "her. It's a replay."},
        ]},
    13: {"theme": "LYRA - SLEEPWALKING NIGHTMARE",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Dim hallway, motion-triggered lights flickering. Lyra standing barefoot, hand pressed "
                "flat against the cold wall, eyes half-lidded, expression vacant — moving on reflex. "
                "The corridor stretches behind her into red-gloom. Film grain, deep blacks."),
             "caption": "She walks in her sleep.\n\nAnd her feet know the way.\n\n'I had no memory of "
                        "walking there. Just cold tiles under my feet.'\n\nThe dorm to the west-comm. "
                        "The chair in the abandoned sector. All of it muscle memory from a life she "
                        "wasn't supposed to remember."},
            {"type": "Image", "prompt": image_prompt(
                "Dream-sequence overlay: the sterile white room from her memory, a blurred figure "
                "(Dr. Quill) leaning over a reclined chair, red three-broken-circles insignia on his "
                "collar visible. Lyra strapped in, eyes open but unfocused. Ghostly double-exposure of "
                "the white room behind her real dorm."),
             "caption": "In the white room, the doctor is kind.\n\n'You're doing beautifully. Now let's "
                        "go over it again — your name, your mission, your reason to hate the Council.'\n\n"
                        "She answers before he asks: 'I believe in the Council's cause.'\n\nEven in her "
                        "dreams, she obeys."},
            {"type": "Text-only", "caption":
                "The voice in her sleep is not stress.\n\nIt is command.\n\n'Phase Two. Override confirmed.\n"
                "Red Signal inbound.'\n\nShe fights it now — whispers her own name until the signal fades. "
                        "'Lyra. Lyra Vex.'\n\nThe only word the programming can't overwrite."},
        ]},
    14: {"theme": "FLASHBACK - THE WHITE ROOM",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Soft-focus flashback: the white conditioning room, smooth walls, no shadows. Dr. Quill "
                "(silver hair, thin gloves, pale dusty eyes) adjusts a console behind a reclined chair. "
                "A younger Lyra, eyes half-lidded, lips parted slightly in the blank receiving expression. "
                "The red three-broken-circles insignia barely visible on his collar."),
             "caption": "Memory implant session — Council grade.\n\n'Your parents died in the riot. "
                        "The Council tried to cover it up. That's why you joined the Rebellion.'\n\nEach "
                        "sentence clicks. IMPLANT STABLE. SIGNAL DORMANT."},
            {"type": "Image", "prompt": image_prompt(
                "Close-up on Lyra's wrist — she is writing, fingers smudged with ink, the word 'Bellmore' "
                "in slanted unfamiliar handwriting across her forearm. The neural strip from the med-scan "
                "glows faintly green beside her on the desk."),
             "caption": "She wakes with the word on her tongue.\n\n'Bellmere.'\n\nIt tastes like sun on old "
                        "brick, like a childhood she can't place. It wasn't in her file. It wasn't in her "
                        "training.\n\nAnd yet... it felt like home.\n\nThe most dangerous trigger isn't a "
                        "command — it's a comfort."},
            {"type": "Text-only", "caption":
                "The rebellion was a training theater.\n\nEvery mission. Every loss. Every name she "
                "remembered as family.\n\nFerris: status DECEASED. Kamel: UNLOCATED. Olsen: INACTIVE.\n\n"
                "They were never rebels.\n\nThey were scripts. And she was the star of a story that was "
                "never hers to star in."},
        ]},
    15: {"theme": "MID-MONTH RECAP & BTS",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Group character sheet style: the core ensemble — Lyra (centre, coat collar up), Josie "
                "(right, hand half-extended), Tomas (left, tablet glowing), Wren (back, visor down), "
                "Kael (behind, arms crossed). Stylized matte portrait grid against a red-gloom background, "
                "each face catching a different angle of light. Film grain, desaturated."),
             "caption": "Two weeks in. Here's everyone you've met so far:\n\n1. Lyra — the weapon who "
                        "doesn't know it\n2. Josie — the soldier who lowered his rifle\n3. Tomas — the analyst "
                        "who noticed\n4. Wren — the menace with the visor\n5. Commander Kael — the wall\n"
                        "6. Dray, Quill & the Council — the architects of it all\n\nPlus the command room, "
                        "the white chamber, and the ruins.\n\nWeek 3: the scenes begin. Clips of the actual "
                        "film start dropping.\n\nWhich character should get the first scene clip?"},
            {"type": "Image", "prompt": image_prompt(
                "Behind-the-scenes concept mood: the production desk — scattered script pages with RED "
                "SIGNAL headers, a red emergency beacon, a microdrive on a lanyard, a notebook with "
                "Council glyphs and 'RS-VEX // PHASE I // OBSERVE' scribbled in margins. Warm desk lamp "
                "glow against cold steel."),
             "caption": "How we build the lie.\n\nEach page in this script started as a question: what "
                        "would a weapon that thinks it's human look like? How do you film belief?\n\n"
                        "Answer: one red light at a time."},
            {"type": "Text-only", "caption":
                "Process notes — week 2.\n\nWe generated 27 concept passes before the coat felt right. "
                "Lyra's jacket is too big because she's borrowing everyone's stories and none of them fit "
                "clean.\n\nThe red isn't just colour — it's the only thing the camera trusts.\n\nComing "
                "next: the white room. The chair. The voice that taught her to obey."},
        ]},
    16: {"theme": "SCENE: FIRST ENCOUNTER",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "12-second scene: rain-slick ruined street, Lyra crouched under a collapsed balcony, "
                "bruise on her side. A drone's red scan-light sweeps — then twitches and drops. Four Order "
                "silhouettes step from the mist. Josie's rifle snaps up. Lyra's hands rise slowly. "
                "Handheld, gritty, film grain.",
                "distant fires crackle, rain patters, drone whine stutters to silence, boot steps in "
                "water, a single whispered 'Go!'"),
             "caption": "First words.\n\n'I escaped. I have proof.'\n\nThey could have shot her on sight. "
                        "Instead, Josie lowered his rifle.\n\nThat small mercy is the first crack in the "
                        "Order's certainty — and the first step of hers."},
            {"type": "Image", "prompt": image_prompt(
                "Close two-shot: Wren's armored glove gripping Lyra's elbow, both faces inches apart — "
                "Wren's visor hiding her eyes, Lyra's wide pupils reflecting the red emergency light. "
                "Tension coiled like a spring."),
             "caption": "Trust is earned in half-gestures.\n\nWren could have broken her wrist. Instead "
                        "she tests her reaction time.\n\n'Don't get lost.'\n\nThe first lie they'll all tell "
                        "themselves is that it meant nothing."},
            {"type": "Text-only", "caption":
                "She felt something sharp flicker across her chest.\n\nNot fear. Recognition.\n\nJosie "
                "didn't know it then — but the handler's grip she just felt was the first thing in months "
                "that recognized her name.\n\nNot Lyra.\n\nNot yet.\n\nThe signal is patient. It always "
                "returns to the frequency of home."},
        ]},
    17: {"theme": "SCENE: THE JACKET",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "10-second scene: Lyra standing by the observation deck railing at night, wind whipping her "
                "coat. Josie approaches, hands her a steaming metal cup. The compound lights pulse red in "
                "the valley below. She doesn't smile, but her shoulders drop half an inch.",
                "wind through the ridge, cup metal clink, distant compound hum, her breath steady"),
             "caption": "He handed her a cup like it was ammunition.\n\n'Synth-lemon. Tastes like melted "
                        "plastic and nostalgia.'\n\nShe almost smiled.\n\nThat almost is the first real "
                        "thing she's felt in six months."},
            {"type": "Image", "prompt": image_prompt(
                "Medium: Josie sitting on the edge of her bunk the next morning, holding a wrapped "
                "jacket. Lyra's bare feet on the concrete floor, the datapad Josie slipped her between "
                "them. Early morning grey light through a vent."),
             "caption": "The jacket is too big.\n\nIt belonged to someone who understood the weight of "
                        "silence.\n\n'They said I wasn't ready. But you are, aren't you?'\n\nHe doesn't "
                        "know he's handing her more than warmth — he's handing her a place to hang the "
                        "person she might become."},
            {"type": "Text-only", "caption":
                "'Not everyone comes back from that kind of conditioning.'\n\nHe said it like he meant "
                "the coat, not her.\n\nBut she heard the rest: *I still see you. I'm still trying.*\n\n"
                "Some offers don't need to be spoken. They just need to be kept — folded at the shoulders, "
                "waiting by the door."},
        ]},
    18: {"theme": "SCENE: RED ALERT LOCKDOWN",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "15-second sequence: facility lights snap from dim to full white, a long red strobing "
                "alert 'SECURITY LEVEL: SPLINTER' across every corridor. Lyra jolts upright in her bunk, "
                "face pale. Camera tilts down her body to the panel behind the mirror — scratched metal "
                "showing 'RS-VEX // PHASE I // OBSERVE'.",
                "harsh strobing light, mechanical voice 'SECURITY LEVEL: SPLINTER', her ragged breathing, "
                "metal door hissing shut"),
             "caption": "The phrase wasn't a dream.\n\n'Asset Vex, hold still. Red Signal active. Override "
                        "engaged.'\n\nFacility-wide alarm: SPLINTER PROTOCOL. But her body moved before "
                        "her mind caught up — straight to the mirror, straight to the panel, straight to "
                        "the chair she remembers."},
            {"type": "Image", "prompt": image_prompt(
                "Wide shot: the abandoned auxiliary sector doorway, Old-Sector sign flickering. The "
                "strapped chair with cranial interface ports half-hidden in dust sheets, bathed in the "
                "flickering emergency red. Lyra has just backed away, face white."),
             "caption": "She saw it before she saw herself.\n\nThe chair. The restraints. The cranial "
                        "ports like eyes.\n\n'Something sharp flickered across her chest — like panic, "
                        "but deeper. Not fear. Recognition.'\n\nThe Order built their base on Council "
                        "blueprints. Some ghosts come pre-installed."},
            {"type": "Text-only", "caption":
                "'Do not deviate.'\n'Observe until recall.'\n'Await confirmation.'\n\nNo one spoke. These "
                "were not memories — they were muscle-memory commands, filed away by a brain that didn't "
                "know it was keeping score.\n\nShe gripped her sink until her knuckles went white.\n\n"
                "Not her thoughts.\n\nNot her house.\n\nBut her hands? Her hands were home."},
        ]},
    19: {"theme": "SCENE: INTERROGATION",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "13-second scene: Room Seven — two chairs, no monitors. Lyra sits across from Tomas, "
                "his eyes unreadable behind safety-glass. A single overhead light casts both their "
                "shadows on the wall. She answers calmly.",
                "room HVAC hum, chair leather creak, pen on paper, her steady breathing"),
             "caption": "Pixels don't twitch when they lie.\n\nTomas said it like a test. It felt like an "
                        "invitation.\n\n'Tell me your earliest memory after escaping Council detainment.'\n\n"
                        "Every answer she gave was a brick in a wall she didn't know she was building."},
            {"type": "Image", "prompt": image_prompt(
                "Close on Lyra's hands — one folded in her lap, the other curled tight around a hidden "
                "micro-drive. The interrogator's gloved finger taps a file labeled 'VEX/DELTA-EXTRACT "
                "/ LEVEL 2 CONDITIONED' before it collapses to static."),
             "caption": "Some files delete themselves.\n\n'Level 2 Conditioned. Raw memory repatterning. "
                        "Behavioral redirection. Rebellion simulation.'\n\nA ghost built into someone's "
                        "reality.\n\nThe folder vanished the moment he tried to hold it. Some truths "
                        "aren't allowed to be saved."},
            {"type": "Text-only", "caption":
                "'What do you see when you're alone?'\n\n'A room with no walls. A voice that doesn't "
                "have a face. The phrase Red Signal repeating in my head, but I don't know why.'\n\n"
                "He logged it without blinking: 'She doesn't know.'\n\nThat's the most dangerous thing "
                "he could have written — because she's sitting right across from the man who decided "
                "to keep it that way."},
        ]},
    20: {"theme": "SCENE: COMBAT FLOW",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "12-second sequence: the training deck, obstacles and pop-up targets under harsh light. "
                "Lyra moves between them like she owns the space — fluid, precise, no wasted motion. "
                "A flashbang proxy bursts nearby; she doesn't flinch.",
                "PA buzzer, burst-round reports, foam impacts, sensor-mine bleeps, the flat whine of "
                "readouts"),
             "caption": "She hit the beacon first.\n\nToo first.\n\n'Muscle memory. From where? Your fake "
                        "Rebellion?'\n\nWren called it cute. Cute is the sound of your enemy being "
                        "carefully, efficiently disassembled."},
            {"type": "Image", "prompt": image_prompt(
                "Split-screen: on the left, Lyra finishing the course, weapon low, face blank. On the "
                "right, the biometric overlay — heart rate 89, flat line, no spike. Wren and Josie "
                "watching from opposite ends, expressions unreadable."),
             "caption": "89 beats per minute.\n\nEven under simulated fire. Even with a flashbang ten "
                        "feet away.\n\n'A recruit doesn't get that ready for chaos.'\n\nShe wasn't born "
                        "to this fight. It was rehearsed.\n\nAnd rehearsal leaves no scar — only muscle."},
            {"type": "Text-only", "caption":
                "Tomas rewound the footage three times.\n\n'Too clean. Too prepared.'\n\n'Pattern matches "
                "conditioning protocol alpha-variant. Suggest further behavioral testing under emotional "
                "duress.'\n\nThe recommendation was signed and filed — but not shared.\n\nSome tests "
                "are performed in silence, by doctors who watch a woman run a course she's already run "
                "a hundred times in her sleep."},
        ]},
    21: {"theme": "AUDIO & SOUND DESIGN",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "9-second wide corridor shot: a single red emergency light strobing, thin smoke drifting "
                "through the beam, cold concrete and steel. Slow push-in through the haze, locked-off "
                "surveillance feel. Deep blacks, desaturated, film grain.",
                "layered — low electrical hum, distant klaxon, a soft rhythmic heartbeat, ash-like rain"),
             "caption": "Close your eyes.\n\nHear it? The hum. The pulse. The rain that falls like ash.\n\n"
                        "Sound is half the film. Every clip carries native stereo audio — hums, footsteps, "
                        "heartbeats, whispers.\n\nThis is what the base sounds like when nobody's talking."},
            {"type": "Image", "prompt": image_prompt(
                "Audio waveform visualization: a heartbeat traced across a dark screen, overlaid with "
                "the glyphic pulse of a Red Signal phrase. Red light pulses in sync with the rhythm. "
                "Textured grain overlay."),
             "caption": "One rhythm. Two sources.\n\nHer heartbeat — and the one that lives beneath it, "
                        "in the hollow behind her ribs, coded and patient.\n\n'The pressure behind my "
                        "eyes had returned... like her memories were expanding too fast for her skull "
                        "to contain.'\n\nListen close. That's not fear.\n\nThat's the signal."},
            {"type": "Text-only", "caption":
                "Design note — the sound of control.\n\nThe base hums at 47 Hz: just below hearing, just "
                "above comfort. It carries the alert tone, the filtered air, the flicker of a camera "
                "that never blinks.\n\nWe record real stereo on every clip — because the most important "
                "dialogue in RED SIGNAL is the silence between the words.\n\nWhat does your heartbeat "
                "sound like when it's not yours?"},
        ]},
    22: {"theme": "THE CHIP ACTIVATION",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "8-second close: the black micro-drive on a metal table, faint green glyph pulsing. "
                "Lyra's finger hovers over it, trembling. The chip sparks once, bright, the glyph flares.",
                "low electronic whine rising to a chirp, the soft spark of a chip, her breath catching"),
             "caption": "Her skin remembered it first.\n\n'The chip... it was warm. A faint pulse in her "
                        "fingers as if the chip recognized her skin.'\n\nThe drive Josie found in her "
                        "medkit — warm, pulsing, alive with a green glyph that no code taught her to read."},
            {"type": "Image", "prompt": image_prompt(
                "Extreme close: the scorched remains of the chip in a metal cup, steaming, black coils. "
                "Lyra's palm visible, the green glyph still faintly glowing on her skin. Background: the "
                "dorm mirror, dark."),
             "caption": "It burned itself out.\n\n'Echo vector aligned. Anchor acquired. Initial tether "
                        "complete. Command hierarchy unlocked.'\n\nHer voice — but not her.\n\nThe chip is "
                        "ash. But the words it left behind are still burning."},
            {"type": "Text-only", "caption":
                "The worst part wasn't the voice.\n\nIt was how much she wanted to obey it.\n\n'You're "
                "not supposed to survive this.'\n'There's a version of her the public already believes in.'\n\n"
                "Phase Two isn't coming.\n\nPhase Two is already here.\n\nAnd it's wearing her face."},
        ]},
    23: {"theme": "TOMAS - THE INVESTIGATION",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Tomas at his bank of monitors, face lit blue, safety-glasses reflecting scrolling data. "
                "He's overlaying blackout timestamps with Sayen's logged locations — the pattern lines up "
                "perfectly. His expression is grim realization."),
             "caption": "Tomas found the pattern.\n\n'Sayen always shows up right before the lights go out.'\n\n"
                        "Not a guard. A trigger.\n\n'The blackout wasn't external sabotage. It was coming "
                        "from her.'"},
            {"type": "Image", "prompt": image_prompt(
                "Close on a terminal screen: an ION-SIGNAL.CONFIRMED tag pulsing red, overlaid on a "
                "spike in Lyra's cortical activity during a fugue. The cursor hovers over 'ACTIVE?'."),
             "caption": "ION-SIGNAL.CONFIRMED.\n\nThe tag that doesn't exist in any Order database. The "
                        "signal that's been riding her neural spikes, quiet as a whisper, persistent as a "
                        "heartbeat.\\n\\n'Not just outbound signals. It received real-time command feeds.'"},
            {"type": "Text-only", "caption":
                "He didn't trust the system anymore.\n\nNot with what he was starting to see.\n\nHe opened "
                "a hidden subchannel. 'This is Tomas. We need to talk. No eyes. Archive C.'\n\nSome truths "
                "are too heavy for the light. They have to be carried in the dark — between two men who "
                "just realized the war inside Lyra's head was never an accident."},
        ]},
    24: {"theme": "ARCHIVE C",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Wide: the Archive C chamber — dust-layered steel shelves, unopened crates, flickering "
                "motion-strips. A rotating holo of Lyra's biometric fluctuations pulses in muted red above "
                "a steel table. Kael and Tomas stand over it, faces half-shadow."),
             "caption": "The archive that shouldn't exist.\n\n'Project Echo. She was one of six.'\n\n"
                        "The holo didn't lie. Her neural scaffolding, her behavioral dampeners, her "
                        "memory loop — all of it logged, all of it watched.\n\nFive are dead. She's the "
                        "last."},
            {"type": "Image", "prompt": image_prompt(
                "Close on the holo display: the file header 'Asset: LYRA VEX. Deployment: ORDER INFILTRATION. "
                "Primary Role: Constructed Defector. Override Status: Active. Command Code: Red Signal - "
                "Phase II. Await Initiation.' Kael's finger hovers over it."),
             "caption": "COMMAND CODE: RED SIGNAL - PHASE II.\n\nAWAIT INITIATION.\n\nThe instruction they "
                        "buried in her marrow. The trigger phrase that lives in her dreams. The role she was "
                        "built to play.\n\nAnd the one she just refused to read from the script."},
            {"type": "Text-only", "caption":
                "Drift Pattern log — 11:47.\n\n'RS-VEX // PHASE I // OBSERVE.'\n\nEtched into the metal "
                "behind her mirror. Scratched by a hand that wasn't hers.\n\n'Override delayed. Continue "
                "observation. Do not initiate.'\n\nThey didn't hide her purpose in encryption.\n\nThey hid "
                "it in plain sight — where she'd find it when she was ready to remember."},
        ]},
    25: {"theme": "THE COLLAPSE",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "14-second scene: Lyra in the infirmary, eyes half-lidded, speaking in full Council code. "
                "Tomas leans close, Josie at her side. The words come like a broadcast: 'Echo vector "
                "aligned. Anchor acquired.' Her nose begins to bleed.",
                "flat electronic voice overlay, her breath hitching, Tomas's whispered 'She was speaking "
                "in code', Josie's sharp intake"),
             "caption": "She spoke in Council.\n\n'Echo vector aligned. Anchor acquired. Initial tether "
                        "complete.'\n\nNot a dream. Not a hallucination. A live broadcast from the program "
                        "they buried in her skull.\n\nAnd then the blood — nosebleed, hot and certain — "
                        "as her body tried to shut the door the voice had opened."},
            {"type": "Image", "prompt": image_prompt(
                "Medium three-shot: Lyra between Tomas and Josie in the medbay, all three pale. The "
                "data-slate between them shows 'ION:// OBSERVE. HOLD.' in red glyphs. A neural strip "
                "glows on the table."),
             "caption": "ION:// OBSERVE. HOLD.\n\nThe tag the system whispered when she was seven hours "
                        "old in their program.\n\n'The rebellion never existed.'\n\n'The anger. The "
                        "missions. Even the friends. They gave me a purpose — then rewrote it. Over and "
                        "over. Until I believed I was fighting back.'\n\nShe had just unmade her entire "
                        "life in a single sentence."},
            {"type": "Text-only", "caption":
                "Josie's hand on her shoulder.\n\n'They didn't take my past... They built it.'\n\n"
                "The words fall like stones into still water. Each ripple a memory that wasn't — a friend "
                "who was a construct, a loss that was a simulation, a love that was a command phrase.\n\n\n\n\n\n"
                "What survives when the foundation is a lie?\n\n\n\n\n\nAnswer: the choice to stop believing."},
        ]},
    26: {"theme": "THE TEAM - TWO-SHOTS",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Warm interior: the four of them at a corner table in the common mess — Lyra, Josie, "
                "Tomas, Wren. Steam rises from synth-coffee. Josie's hand is near her shoulder, not "
                "touching. The lighting is the softest in the whole compound. Four expressions, four "
                "realizations."),
             "caption": "The four who stayed.\n\nEach of them a different kind of rescue: Josie who lowered "
                        "his rifle, Tomas who kept her secrets, Wren who set traps to protect her, and Lyra — "
                        "who finally stopped pretending she needed saving.\n\n'They made you something,' "
                        "she said. 'But they didn't make this.'"},
            {"type": "Image", "prompt": image_prompt(
                "Tight two-shot: Josie and Lyra on the observation deck at dawn. His hand outstretched, "
                "offering it to her. Her expression is the moment before she decides. Wind in their hair, "
                "the compound lights red in the valley below."),
             "caption": "His hand was an anchor.\n\n'I don't know what you are, Lyra. But I know what you've "
                        "done since you got here. You saved people. You told the truth when you didn't have "
                        "to.'\n\nShe took it — and the last of her hesitation died in his palm."},
            {"type": "Text-only", "caption":
                "Tomas: 'She's not a tool. You're not theirs. You get to say no.'\n\nWren: 'Let's decide "
                "who you'll be now. Not what they built.'\n\nJosie: 'I trust you. Even if I don't fully "
                "understand you.'\n\nFour people. Four choices. One question: when the world gives you a "
                "script, do you read your lines — or do you write the next act?\n\nThey chose the ink."},
        ]},
    27: {"theme": "THE COUNCIL - GOLD & BLUE",
        "posts": [
            {"type": "Image", "prompt": image_prompt(
                "Wide authority: the Council directive room — seven black chairs in a half-moon, each "
                "occupied by a figure. At the centre, Director Saren Holt, face in cold blue light, "
                "reading from a translucent slate. Red loops of Lyra's neural data scroll behind him. "
                "Dr. Malen Quill to his left, Envoy Cassel Rynn to his right, the voice of Ion vibrating "
                "in the walls."),
             "caption": "The architects of the lie.\n\nHolt: 'She fractures beautifully. Let her.'\n\n"
                        "Quill: 'She's thinking beyond her design.'\n\nRynn: 'If she breaks further, we "
                        "can't spin her.'\n\nThey watch her neural storms like meteorologists tracking "
                        "hurricanes — calm, clinical, hungry."},
            {"type": "Image", "prompt": image_prompt(
                "Close on Cassel Rynn at the broadcast console, rehearsing his line in the mirror — "
                "'Today, we bring a lost soul home.' Behind him, AI-teleprompt feed scrolls, fake stress "
                "bruising layers onto older surveillance clips on a secondary screen."),
             "caption": "Perception is reality.\n\n'The world loves a rescued traitor more than a rescued "
                        "victim.'\n\nRynn practiced sincerity like a muscle. The cameras sat just above "
                        "his eye-line — forcing him to look upward, evoking trust.\n\nHe was selling her "
                        "back to a world that never knew it had bought her in the first place."},
            {"type": "Text-only", "caption":
                "ION (voice like gravity): 'She was not built to obey. She was built to believe. Obedience "
                "fractures under pressure. Belief weathers.'\n\nHolt: 'Let her break. Then we step in — "
                "not with control, with rescue.'\n\nThe final line of their play: \n\n'We'll rescue the "
                "version of her the public already believes in.'\n\nThey don't need the real Lyra.\n\n"
                "They just need an audience."},
        ]},
    28: {"theme": "TEASER #1 - REVEAL",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "15-second teaser: rapid cuts across RED SIGNAL iconography — pulsing red emergency light "
                "strobing on concrete, the white conditioning chair in sterile light, Lyra's wide-pupil "
                "eyes in the dark, ash-rain falling through a red beam, Josie lowering his rifle, the "
                "green chip glowing in a trembling hand.",
                "heartbeat pulse, klaxons, a rising electronic swell, sudden silence"),
             "caption": "TEASER #1\n\nA signal in the dark.\n\nSomething was built.\n\nSomething is waking "
                        "up.\n\nRED SIGNAL — a sci-fi thriller, one clip at a time.\n\nFull trailer drops "
                        "at the end of the month."},
            {"type": "Image", "prompt": image_prompt(
                "Title card: RED SIGNAL in bold blocky typography, pulsing with a red emergency-light "
                "glitch. Behind it, a collage of the film's key motifs — the white chair, the chip, the "
                "mark on Lyra's back, the bunker terminal. Desaturated, film grain."),
             "caption": "This is not a review.\n\nThis is a warning.\n\nThe signal you're hearing isn't "
                        "static — it's a name. A place. A phrase that lives in the space between a breath "
                        "and a blink.\n\nRED. SIGNAL. \n\nYou were always meant to remember it."},
            {"type": "Text-only", "caption":
                "31 days. 93 posts. Zero lies told.\n\nStarting Monday: the full trailer.\n\nUntil then — "
                "count the red lights. Every frame. Every shadow. Every time her eyes go too wide.\n\n"
                "She's not sleeping.\n\nShe's waiting.\n\nAnd she's almost awake."},
        ]},
    29: {"theme": "TEASER #2 - LYRA",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "12-second character focus: Lyra in three vignettes — hands concealing the drive under her "
                "collar, her reflection glitching in the dorm mirror, her eyes wide and dilated as the "
                "signal phrase rolls off her lips. Red emergency light as the only source.",
                "her breathing, a faint electronic hum, the whisper 'Red Signal... Override...'"),
             "caption": "TEASER #2\n\nLyra Vex in three beats.\n\n1. The drive nobody knows she carries.\n"
                        "2. The reflection that doesn't blink.\n3. The phrase that isn't hers.\n\nShe is not "
                        "who she was built to be. She is not who they hoped she'd become.\n\nShe is something "
                        "else entirely."},
            {"type": "Image", "prompt": image_prompt(
                "Extreme close: Lyra's eye — wide, pupil dilated, the reflection of a red emergency light "
                "flickering in the iris. In the reflection, the ghost of the white room and a blurred "
                "doctor's silhouette."),
             "caption": "Watch the eyes.\n\nThat dilation isn't fear. That's recognition.\n\n'The moment the "
                        "words left her mouth, a sound clicked inside her ears — like a switch turning.'\n\n"
                        "One glance. One pulse. One moment where the woman and the weapon share a gaze."},
            {"type": "Text-only", "caption":
                "'I'm not yours.'\n\nThree words. Eight letters. A lifetime of unbecoming.\n\nThe signal "
                "screams. The chip burns. The voice in her head remembers.\n\nBut she — the part that "
                "wakes up, the part that chooses, the part that fights — she says no.\n\nAgain.\n\nAnd "
                "again.\n\nAnd again."},
        ]},
    30: {"theme": "FULL TRAILER",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "30-second trailer edit: montage of the core beats — bunker smoke, Josie lowering his "
                "rifle in the rain, the white conditioning chair, Lyra's training run with 89bpm flatline, "
                "the dorm mirror glitch, Tomas at his monitors, the red chip glowing, the Ghost Archive "
                "footage reveal, the escape injector, her silhouette on the ridge as the red signal "
                "pulses.",
                "building orchestral-electronic score, heartbeat under bass, rising tension, final silence")
             "caption": "FULL TRAILER — RED SIGNAL\n\n'I don't know where I'm from anymore.'\n\nBuilt to "
                        "believe. Programmed to obey. Conditioned to forget.\n\nBut weapons don't wake up. "
                        "They don't feel doubt. They don't choose their name.\n\nThe signal is active. "
                        "Override engaged.\n\nShe is not their weapon anymore.\n\nRED SIGNAL — coming soon."},
            {"type": "Image", "prompt": image_prompt(
                "Poster-style composite: Lyra Vex standing on the ridge at the center, coat blowing, "
                "the red signal pulsing behind her. In the background, ghosts of the white room, the "
                "training deck, the archive, arranged in a circle. Deep blacks, red accents, film grain."),
             "caption": "One signal. Two masters. Three choices.\n\nShe was the Council's weapon.\n\nThen "
                        "the Order's secret.\n\nNow — nobody's.\n\nThe trailer reveals everything. "
                        "Everything she remembers. Everything they stole.\n\nEverything she takes back."},
            {"type": "Text-only", "caption":
                "The full picture.\n\nBuilt as Echo-Class Weapon VEX. Deployed as a rebel defector. "
                "Watched by a god in the walls, owned by a politician in the sky, triggered by a man who "
                "never existed.\n\nShe has one fight left in her: to remember that the voice in her head "
                "was never hers — and that the choice to listen is the only thing that ever was.\n\nRED "
                "SIGNAL — Act 2 begins after the credits."},
        ]},
    31: {"theme": "FINALE & WHAT'S NEXT",
        "posts": [
            {"type": "Video", "prompt": video_prompt(
                "15-second epilogue: Lyra in the ash-rain ruins, back to camera, worn grey coat, short "
                "dark hair. She turns her head slightly as a red signal pulses on the horizon. The camera "
                "holds on the silhouette, rain falling, then slow fade to the pulsing red light.",
                "wind, ash-rain, a soft heartbeat, a single whispered line: 'I don't know where I'm from "
                "anymore.'"),
             "caption": "EPILOGUE\n\n'I don't know where I'm from anymore.'\n\nOne month. Thirty-one posts. "
                        "A story told in clips.\n\nThis isn't the end. It's the signal that Act 2 is coming.\n\n"
                        "Thank you for watching RED SIGNAL."},
            {"type": "Image", "prompt": image_prompt(
                "Wide: the ridge at dawn — Lyra's silhouette against a bruised sky, the red pulse on the "
                "horizon answering her signal. Below, the ruined city, broken towers like teeth. Ash-rain "
                "falling. Her coat flares in the wind. Deep blacks, red accent only."),
             "caption": "The signal stays on.\n\nBut now she holds the key.\n\nBehind her: the Order, "
                        "falling. The Council, rising. Ahead: the frost belt, the unknown.\n\nOne woman. "
                        "One choice. One question that echoes across both their worlds:\n\nWho are you "
                        "when nobody's written your lines?\n\nFind out in Act 2."},
            {"type": "Text-only", "caption":
                "RED SIGNAL — ACT 1 COMPLETE.\n\nWhat's next:\n• Act 2, Episodes 1-37 — the war both "
                "sides thought they were fighting\n• The full 38-scene storyboard drop (behind the scenes)\n"
                "• Lyra's character-design evolution — from concept to screen\n\nDrop a 🔴 if you're ready "
                "to walk through the fire with her.\n\nThe signal is patient. It always returns to the "
                "frequency of home.\n\nSee you in Act 2."},
        ]},
}


# ---------------------------------------------------------------------------
# FILE WRITERS
# ---------------------------------------------------------------------------

def write_film_part(p):
    lines = []
    lines.append("=" * 60)
    lines.append("RED SIGNAL - FILM PRODUCTION PROMPT")
    lines.append(f"Part {str(p['n']).rjust(2, '0')} | {p['title']} | {p['subtitle']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"CHAPTER: {p['chapter']}")
    lines.append("")
    lines.append("— SHOTS —")
    for i, s in enumerate(p["shots"], 1):
        lines.append(f"{i}. {s}")
    lines.append("")
    if p.get("audio"):
        lines.append(f"Audio: {p['audio']}")
        lines.append("")
    if p.get("line"):
        lines.append(f"LINE: {p['line']}")
        lines.append("")
    lines.append("FILM NOTE: " + p["note"])
    return "\n".join(lines) + "\n"


def write_post(day, post_idx, post):
    lines = []
    d = date(2026, 8, 15) + timedelta(days=day - 1)
    date_str = d.strftime("%a %b %d")
    iso = d.strftime("%Y-%m-%d")
    lines.append("=" * 60)
    lines.append("RED SIGNAL - SOCIAL MEDIA POST")
    lines.append(f"Day {day} | {date_str} | {iso} | {POSTS[day]['theme']}")
    lines.append(f"POST {post_idx}")
    lines.append("=" * 60)
    lines.append("")
    lines.append("--- POST SETUP ---")
    lines.append(f"DATE: {date_str}")
    lines.append(f"DAY: {day} of 31")
    lines.append("")
    lines.append("--- MEDIA ---")
    lines.append(f"TYPE: {post['type']}" + (f" (8-15s)" if post["type"] == "Video" else ""))
    if post["type"] in ("Image", "Video"):
        lines.append("GEN TOOL: Gemini (image generation)" if post["type"] == "Image"
                     else "GEN TOOL: MiniMax H3 (image/video to video) via ComfyUI Cloud")
        if post["type"] == "Video":
            lines.append("WORKFLOW: workflows/minimax_h3_i2v_lyra.json (or text-to-video variant)")
        lines.append("")
        if post["type"] == "Image":
            lines.append("--- IMAGE PROMPT ---")
            lines.append(post["prompt"])
        else:
            lines.append("--- VIDEO PROMPT ---")
            lines.append(post["prompt"])
        if post.get("ref"):
            lines.append("")
            lines.append("--- REFERENCE IMAGE ---")
            lines.append(post["ref"])
    else:
        lines.append("TYPE: Text-only post (no media needed)")
        lines.append("")
    lines.append("")
    lines.append("--- CAPTION ---")
    lines.append("FB CAPTION:")
    lines.append(post["caption"])
    return "\n".join(lines) + "\n"


def main():
    # Film parts
    fp_dir = ROOT / "film_parts"
    fp_dir.mkdir(exist_ok=True)
    for p in FILM_PARTS:
        (fp_dir / f"part_{str(p['n']).rjust(2, '0')}.txt").write_text(write_film_part(p), encoding="utf-8")
    print(f"Wrote {len(FILM_PARTS)} film parts")

    # Posts: 31 days x 3
    posts_dir = ROOT / "posts"
    for day in range(1, 32):
        dd = posts_dir / str(day).rjust(2, "0")
        dd.mkdir(parents=True, exist_ok=True)
        for i, post in enumerate(POSTS[day]["posts"], 1):
            (dd / f"post_{i}.txt").write_text(
                write_post(day, i, post), encoding="utf-8"
            )
    total = sum(len(POSTS[d]["posts"]) for d in range(1, 32))
    print(f"Wrote {total} posts across 31 days")

    # Detail library
    dl = ROOT / "posts" / "detail_library.md"
    with dl.open("w", encoding="utf-8") as f:
        f.write("# RED SIGNAL - Shared Prompt Detail Library\n\n")
        f.write("House style:\n" + STYLE + "\n\n")
        f.write("## Character blocks\n")
        for k, v in CHAR.items():
            f.write(f"### {k}\n{v}\n\n")
    print(f"Wrote detail library")


if __name__ == "__main__":
    main()
