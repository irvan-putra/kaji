# Models so far

Checked 21 November 2026. Public generic reference only. No model calls or downloads, no private test inputs/results or device details. Daya links only.

## MobileBERT uncased MNLI

Xenova ONNX model_quantized.onnx, int8, 26,967,165 bytes

No license declared on the exact Xenova or typeform model-card metadata checked. Do not infer one from the MobileBERT architecture or a runtime license.

Ranks candidate labels. It does not write JSON or code; a separate extractor and validator must handle the details.

https://huggingface.co/Xenova/mobilebert-uncased-mnli
https://huggingface.co/typeform/mobilebert-uncased-mnli

## SmolLM2-135M-Instruct

bartowski GGUF Q4_K_M, 105,454,432 bytes. Other quants differ.

Apache 2.0 base model. Preserve applicable notices and check conversion provenance.

Compact instruction model, mainly English. Small size does not establish recipe accuracy, multilingual quality or phone speed.

https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct
https://huggingface.co/bartowski/SmolLM2-135M-Instruct-GGUF

## SmolLM2-360M-Instruct

bartowski GGUF Q2_K, 218,674,080 bytes. Q3_K_M is 234.7 MB; Q4_K_M is 270.6 MB.

Apache 2.0 base model. Quantization quality varies; a smaller file is a different configuration.

The optional Daya in-page route currently references Q2_K. Availability in a route is not proof of reliable interpretation or physical-phone performance.

https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct
https://huggingface.co/bartowski/SmolLM2-360M-Instruct-GGUF

## Gemma 3 270M IT

Unsloth GGUF Q2_K, 237,079,584 bytes. Q4_K_M is 253.1 MB. These are current artifacts, not all possible conversions.

Gemma terms, not Apache 2.0. Check the exact model terms, access conditions and conversion notices before use or redistribution.

The 270M size takes text, not image input; do not transfer the larger Gemma family vision claims to this model. Public card lists a 32K context. No integration or suitability claim.

https://huggingface.co/google/gemma-3-270m-it
https://huggingface.co/unsloth/gemma-3-270m-it-GGUF

## Qwen2.5-0.5B-Instruct

Official Qwen GGUF q4_k_m, 491,400,032 bytes. That is 468.6 MiB in binary units, explaining an approximately 469-size label. Sizes here use decimal MB consistently.

Apache 2.0 model-card declaration. Check notices for the chosen conversion and runtime.

Multilingual instruction model. Its exact card lists 32,768 context tokens and up to 8,192 generated tokens, not the larger family headline of 128K. No model is loaded by this catalog.

https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF

## Inkling 2 Mini

Unsloth 1-bit: 7.76 GB; 2-bit: 8.49 GB; recommended 4-bit: 17.63 GB. Official mixed NVFP4/MXFP8 checkpoint: about 20 GB. ggml-org 4-bit: 17.6 GB. Vision projectors add separate downloads.

Apache 2.0 open weights. Released 20 Nov 2026. Runtime and conversion support still need checking for the exact artifact.

Desktop/local-server class, not a lightweight Daya in-page replacement. Official guidance supports Apple silicon with 32GB+ memory and recommends 32GB+ VRAM on other GPUs. Unsloth gives lower quant-dependent combined-memory estimates, starting around 9GB for 1-bit; these are not conflicting requirements for the same configuration. No phone/browser or current Daya WASM compatibility established.

https://huggingface.co/thinkingmachines/Inkling-2-Mini
https://unsloth.ai/docs/models/inkling-2-mini
https://huggingface.co/ggml-org/Inkling-2-Mini-GGUF
