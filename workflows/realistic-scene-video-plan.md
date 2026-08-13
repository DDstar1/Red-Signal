# Mirror Panel Reveal — Video Stage

## Source still
Output of `realistic-scene-sdxl-facedetail.json` (SDXL + skin realism LoRA + FaceDetailer).

## Video motion prompt
She stares at the faint etched text scratched into the metal behind the panel, breath catching audibly. Her hand, already braced against the wall, tightens as a wave of vertigo visibly hits her — her eyes lose focus, head tilting slightly off-balance. She stumbles back half a step, shoulder catching the wall for support. The cool clinical light flickers faintly overhead. Her expression shifts from shock to disoriented fear, lips parting as if to speak but no sound comes. Camera holds a static medium shot throughout — no movement, no cuts, letting the physical reaction play out in real time.

## How to run (once credits are available)
`run_template` with `name: "video_ltx2_3_i2v"`, `slot_overrides`:
- `320.input` = the still image (use `use_previous_output` with the still's `prompt_id` once generated)
- `320.text` = the motion prompt above
- `320.value_1` = 1216, `320.value_2` = 832 (matches the still's resolution — swap if you want a different aspect)

## Next step after this clip
Extract the last frame (`get_any_video_frame` blueprint, `value` = -1), look at it, and write the next prompt adaptively — same method as the chip scene chain (see `chipscene-video-chain-plan.md`).
