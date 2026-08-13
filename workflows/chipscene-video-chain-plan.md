# Red Signal — Chip Scene Video Chain (Adaptive Method)

## Story overview (loose guide, not a script)
Lyra Vex holds a data chip that begins glowing green. As it activates, she starts bleeding from the nose, growing faint. She loses her grip and drops the chip. Disoriented, she staggers and reaches for support. She catches herself against a wall, breathing hard, and finally lifts her head to look at the camera — dazed, shaken, alive. Red ambient light dominates throughout; green light is tied specifically to the chip and fades as it goes dark.

This overview exists to keep every stage pointed in the same direction — it is NOT a fixed shot list. The actual content of each stage is decided by what the previous stage's last frame actually shows.

## The process (repeat per stage)
1. Run the video generation for this stage (starting image = last frame of the previous stage, or the Stage 1 still for the very first stage).
2. Extract the **last frame** of the resulting clip (`get_any_video_frame` blueprint, `value` = -1).
3. **Look at that actual frame** — her pose, expression, framing, lighting, how far the story has visibly progressed.
4. Write the **next stage's prompt** based on what's really in that frame, nudging the action forward toward the next beat in the overview above. Don't assume continuity that isn't actually there in the frame — react to it.
5. Move to the next stage.

This keeps the story on track without fighting the model to hit an exact pre-written script it may not have produced.

## Stage 1 — Still image (fixed starting point, already saved: chipscene-stage01-image.json)
lyravex, extreme close-up cinematic still of a woman with short dark choppy pixie hair, sharp angular cheekbones, and pale translucent skin catching cold ambient light. She wears a weathered olive-brown utility jacket with a frayed high collar and visible stitching, worn over a plain black top. She stands in a dim concrete room with rough unfinished walls, faint red emergency lighting bleeding in from an unseen source off-frame, casting long soft shadows across her jaw and throat. In her open palm rests a small matte-black data chip, its surface etched with faint circuitry lines, pulsing a cold green light that reflects wetly in her dark eyes. Her expression is intensely focused, brows drawn slightly, breath visible in the cool air. Shallow depth of field, 35mm anamorphic lens flare bleeding faintly at the frame edges, heavy film grain, desaturated color grade with crushed blacks and red-green complementary accents, atmospheric haze drifting through the beam of light.

## Stage 1 — Video motion prompt (fixed starting point)
The camera holds a locked-off close shot on her face and the chip in her palm. The chip's green glow pulses brighter in slow rhythmic waves, casting shifting light across her cheek and jaw. A single thin line of dark red blood begins to bead at her left nostril and slowly trace downward, catching the green light as it moves. Her eyes remain fixed on the chip, unblinking, pupils faintly dilated. Her breathing is shallow, chest rising in short controlled movements. Fine dust motes drift through the beam of ambient light behind her. No camera movement, no cuts — a continuous, unbroken close shot building tension.

## Stages 2-5
Not pre-written — determined live, one at a time, by looking at each stage's actual last frame per the process above. Run when credits are available; I'll view each result and write the next prompt in response.

## Technical reference
- Video model: LTX-2.3, template name `video_ltx2_3_i2v`
- Run via `run_template` with `slot_overrides`: `320.input` = starting image, `320.text` = motion prompt, `320.value_1` = 1280, `320.value_2` = 720
- Last-frame extraction: `get_any_video_frame` subgraph blueprint, `video` = previous stage's output, `value` = -1

## After all stages are generated
Stitch clips in sequence in a video editor — straight cuts, no transitions needed since each clip starts exactly where the previous one ended.
