# Privacy policy

This plugin sends your requests to Liquid Inference, at `https://router.inference.ai.exchange/v1` unless you set another API base URL.

## What the plugin sends

- The prompt, the model parameters and any tool definitions in each request.
- Your Liquid API key, in the `Authorization` header.
- The headers `X-Title: Dify` and `HTTP-Referer: https://dify.ai/`. Liquid Inference shows the title on your receipts.

## What the plugin stores

The plugin stores nothing. Dify keeps your API key as a credential. The plugin does not log prompts or answers.

## What Liquid Inference does with the data

Liquid Inference passes each request to the model provider that wins the auction for it. The provider receives the prompt. See the Liquid Inference terms and privacy policy at https://liquidinference.ai for how the exchange and the providers handle request data.

## Contact

Open an issue at https://github.com/architect-xyz/liquid-dify-plugin/issues.
