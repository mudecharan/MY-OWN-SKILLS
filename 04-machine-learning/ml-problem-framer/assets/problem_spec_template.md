# ML Problem Specification — <project>

## 1. Decision-first framing
| Item | Answer |
|---|---|
| Decision the prediction enables | |
| Who acts on it, how often | |
| Action lead time required | |
| What happens today (manual process) + its error rate | |

## 2. Target engineering
| Item | Value |
|---|---|
| Target Y defined precisely ("churned = no purchase within 90d of expiry") | |
| Label availability in data (yes/no + quality) | |
| Prediction horizon (must exceed action lead time!) | |
| Class balance | |
| Label latency (when does truth arrive) | |

## 3. Unit & leakage contract
- One row = one <entity> at time <t>
- Feature availability timeline: every feature timestamped; anything post-t is BANNED

| Feature | Available from | Leak risk |
|---|---|---|

## 4. Feasibility verdict
| Check | Result |
|---|---|
| Signal audit (do similar features predict Y historically?) | |
| Volume (enough positives?) | |
| Rules could do this instead? (then build rules) | |
| GO / NO-GO for ML | |

## 5. Success bar
"Deploy if we beat current process by ____ (measured in business value:
e.g., catch 30% more churners at equal contact budget)."
