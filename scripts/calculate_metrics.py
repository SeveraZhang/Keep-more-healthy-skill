#!/usr/bin/env python3
"""Transparent estimate calculator for the weight-loss-coach skill."""

import argparse
import json

ACTIVITY = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "very_active": 1.725,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sex", choices=["female", "male"], required=True)
    parser.add_argument("--age", type=float, required=True)
    parser.add_argument("--height-cm", type=float, required=True)
    parser.add_argument("--weight-kg", type=float, required=True)
    parser.add_argument("--activity", choices=ACTIVITY, default="light")
    parser.add_argument("--waist-cm", type=float)
    parser.add_argument("--goal-weight-kg", type=float)
    args = parser.parse_args()

    if min(args.age, args.height_cm, args.weight_kg) <= 0:
        parser.error("age, height, and weight must be positive")
    sex_adjustment = 5 if args.sex == "male" else -161
    bmr = 10 * args.weight_kg + 6.25 * args.height_cm - 5 * args.age + sex_adjustment
    bmi = args.weight_kg / (args.height_cm / 100) ** 2
    tdee = bmr * ACTIVITY[args.activity]
    result = {
        "method": "Mifflin-St Jeor; estimates only, not medical advice",
        "bmr_kcal_day": round(bmr),
        "activity_factor": ACTIVITY[args.activity],
        "estimated_tdee_kcal_day": round(tdee),
        "suggested_deficit_kcal_day_range": [250, 500],
        "bmi": round(bmi, 1),
    }
    if args.waist_cm:
        result["waist_height_ratio"] = round(args.waist_cm / args.height_cm, 2)
    if args.goal_weight_kg and args.goal_weight_kg < args.weight_kg:
        remaining = args.weight_kg - args.goal_weight_kg
        min_weekly = args.weight_kg * 0.0025
        max_weekly = args.weight_kg * 0.0075
        result["estimated_weeks_to_goal_range"] = [round(remaining / max_weekly), round(remaining / min_weekly)]
        result["timeline_note"] = "Update after at least two weeks of trend data; weight change is not linear."
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

