#!/usr/bin/env bash
while :; do
  qwen --yolo || true
  echo "[qwen exited or errored; restarting...]"
  sleep 1
done
