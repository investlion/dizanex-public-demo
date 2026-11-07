"""Static, illustrative records for the standalone Codester preview."""

from __future__ import annotations

from typing import Any


SAMPLE_SIGNALS: list[dict[str, Any]] = [
    {
        "id": "SAMPLE-001", "pair": "BTCUSDT", "direction": "LONG",
        "entry": 67120.0, "stop_loss": 66350.0, "tp1": 68400.0,
        "tp2": 69680.0, "tp3": None, "confidence": 89.0,
        "risk": "MEDIUM", "timestamp": "2025-03-18 09:15 UTC",
        "trend": "BULLISH", "regime": "TRENDING",
    },
    {
        "id": "SAMPLE-002", "pair": "ETHUSDT", "direction": "SHORT",
        "entry": 3542.5, "stop_loss": 3604.0, "tp1": 3420.0,
        "tp2": None, "tp3": None, "confidence": 84.5,
        "risk": "HIGH", "timestamp": "2025-03-18 08:40 UTC",
        "trend": "BEARISH", "regime": "VOLATILE",
    },
    {
        "id": "SAMPLE-003", "pair": "SOLUSDT", "direction": "LONG",
        "entry": 182.4, "stop_loss": 176.8, "tp1": 191.0,
        "tp2": 199.5, "tp3": 208.0, "confidence": 92.0,
        "risk": "LOW", "timestamp": "2025-03-17 21:10 UTC",
        "trend": "BULLISH", "regime": "TRENDING",
    },
    {
        "id": "SAMPLE-004", "pair": "XRPUSDT", "direction": "SHORT",
        "entry": 2.31, "stop_loss": 2.39, "tp1": 2.18,
        "tp2": 2.06, "tp3": None, "confidence": 81.0,
        "risk": "MEDIUM", "timestamp": "2025-03-17 16:25 UTC",
        "trend": "BEARISH", "regime": "RANGING",
    },
    {
        "id": "SAMPLE-005", "pair": "LINKUSDT", "direction": "LONG",
        "entry": 18.72, "stop_loss": 18.05, "tp1": 19.85,
        "tp2": None, "tp3": None, "confidence": 86.5,
        "risk": "MEDIUM", "timestamp": "2025-03-17 12:05 UTC",
        "trend": "BULLISH", "regime": "TRENDING",
    },
    {
        "id": "SAMPLE-006", "pair": "BTCUSDT", "direction": "LONG",
        "entry": 66880.0, "stop_loss": 66020.0, "tp1": 67900.0,
        "tp2": 69050.0, "tp3": None, "confidence": 78.0,
        "risk": "HIGH", "timestamp": "2025-03-16 18:30 UTC",
        "trend": "MIXED", "regime": "RANGING",
    },
]

SAMPLE_MARKETS: list[dict[str, Any]] = [
    {"pair": "BTCUSDT", "sample_price": 67480.0, "structure": "HH / HL", "bos": "BOS UP", "choch": "—", "trend": "BULLISH", "momentum": 0.82, "volume": "EXPANDING", "regime": "TRENDING", "confidence": 89.0},
    {"pair": "ETHUSDT", "sample_price": 3510.2, "structure": "LH / LL", "bos": "—", "choch": "CHoCH DOWN", "trend": "BEARISH", "momentum": 0.68, "volume": "ABOVE AVERAGE", "regime": "VOLATILE", "confidence": 84.5},
    {"pair": "SOLUSDT", "sample_price": 184.7, "structure": "HH / HL", "bos": "BOS UP", "choch": "—", "trend": "BULLISH", "momentum": 0.91, "volume": "EXPANDING", "regime": "TRENDING", "confidence": 92.0},
    {"pair": "XRPUSDT", "sample_price": 2.28, "structure": "RANGE", "bos": "—", "choch": "—", "trend": "MIXED", "momentum": 0.43, "volume": "NORMAL", "regime": "RANGING", "confidence": 81.0},
    {"pair": "LINKUSDT", "sample_price": 18.9, "structure": "HL / RANGE", "bos": "BOS UP", "choch": "—", "trend": "BULLISH", "momentum": 0.73, "volume": "NORMAL", "regime": "TRENDING", "confidence": 86.5},
]

SAMPLE_REJECTIONS: list[dict[str, str]] = [
    {"pair": "ADAUSDT", "reason": "CONFIDENCE_BELOW_THRESHOLD", "timestamp": "2025-03-18 09:02 UTC", "filter": "Confidence 76.0 / sample threshold 83.0"},
    {"pair": "DOGEUSDT", "reason": "RISK_REWARD_NOT_MET", "timestamp": "2025-03-18 08:51 UTC", "filter": "Sample R:R 1.4 / sample minimum 2.0"},
    {"pair": "AVAXUSDT", "reason": "CONFLICTING_STRUCTURE", "timestamp": "2025-03-18 08:43 UTC", "filter": "Higher and lower timeframe directions differ"},
    {"pair": "BNBUSDT", "reason": "STALE_MARKET_INPUT", "timestamp": "2025-03-18 08:21 UTC", "filter": "Sample candle input exceeds freshness window"},
]


def display_value(value: Any) -> Any:
    """Render absent levels as a dash without filling in a value."""
    return "—" if value is None or value == "" else value


def signal_table_row(signal: dict[str, Any]) -> dict[str, Any]:
    return {
        "Pair": signal.get("pair", "—"),
        "Direction": signal.get("direction", "—"),
        "Entry": display_value(signal.get("entry")),
        "Stop loss": display_value(signal.get("stop_loss")),
        "TP1": display_value(signal.get("tp1")),
        "TP2": display_value(signal.get("tp2")),
        "TP3": display_value(signal.get("tp3")),
        "Confidence": display_value(signal.get("confidence")),
        "Risk": display_value(signal.get("risk")),
        "Sample timestamp": display_value(signal.get("timestamp")),
    }


def filter_signals(
    signals: list[dict[str, Any]], *, pair: str = "All pairs",
    direction: str = "All directions", minimum_confidence: float = 0,
) -> list[dict[str, Any]]:
    return [
        row for row in signals
        if (pair == "All pairs" or row.get("pair") == pair)
        and (direction == "All directions" or row.get("direction") == direction)
        and float(row.get("confidence") or 0) >= minimum_confidence
    ]


def signal_preview(signal: dict[str, Any]) -> str:
    lines = [
        "DIZANEX SAMPLE SIGNAL — DEMO ONLY",
        f"{signal.get('pair', '—')} | {signal.get('direction', '—')}",
        f"Entry: {display_value(signal.get('entry'))}",
    ]
    for label, key in (("Stop loss", "stop_loss"), ("TP1", "tp1"), ("TP2", "tp2"), ("TP3", "tp3")):
        if signal.get(key) is not None:
            lines.append(f"{label}: {signal[key]}")
    lines.extend([
        f"Confidence: {display_value(signal.get('confidence'))}",
        f"Risk: {display_value(signal.get('risk'))}",
        f"Sample timestamp: {display_value(signal.get('timestamp'))}",
    ])
    return "\n".join(lines)
