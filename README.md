# Liquid Inference

Liquid Inference is an auction exchange for LLM inference. Providers post standing offers. The exchange ranks the eligible offers for each request, sets a price cap before the first token, and charges for the tokens used.

This plugin adds Liquid Inference as a model provider in Dify.

## Setup

1. Create a workspace on Liquid Inference, add a balance, and create a `spend` key.
2. In Dify, open **Settings > Model Provider** and install **Liquid Inference**.
3. Paste the key in **API Key**. Leave **API Base URL** empty to use `https://router.inference.ai.exchange/v1`.

## Models

`liquid.auto` is in the list. It lets the exchange choose the model for each request.

To use another model, choose **Add Model** and enter its name exactly as `GET /v1/models` returns it. Set the context size and the features of that model.

## Cost

The exchange sets a cap on each request. It sends the cap in the `x-liquid-cap-usd` response header. To limit total spend, set a spending limit on the key.

## Payments

The plugin makes no payments and moves no funds. It sends chat requests only. Liquid Inference bills your Liquid workspace balance, which you manage on the Liquid Inference site.

## Source

https://github.com/architect-xyz/liquid-dify-plugin
