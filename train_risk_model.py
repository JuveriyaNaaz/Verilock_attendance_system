"""
Trains a small ML model that predicts whether a student is likely to fall
below 75% overall attendance by the end of the semester, based only on
their attendance pattern from the first few weeks.

Why simulated data? A brand-new attendance system has very few real
records to learn from. So we simulate a semester's worth of plausible
student attendance behavior, train on that, and use the trained model
to score real students as their real data comes in. This is a common,
defensible approach when real historical data doesn't exist yet.

Run this once (or whenever you want to retrain):
    python train_risk_model.py
It saves a file called risk_model.pkl, which app.py loads at runtime.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

np.random.seed(42)

SESSIONS_PER_SEMESTER = 60
EARLY_WINDOW = 15          # we only "see" the first 15 sessions as features
NUM_SYNTHETIC_STUDENTS = 2000


def simulate_one_student():
    """
    Each synthetic student has a hidden 'reliability' score (how likely
    they are to attend any given session). We use this to generate a
    session-by-session attendance record for a full semester.
    """
    reliability = np.random.beta(a=5, b=2)  # skewed toward higher attendance, like real classes
    # small day-to-day noise so it's not perfectly consistent
    daily_attendance = np.random.rand(SESSIONS_PER_SEMESTER) < (reliability + np.random.normal(0, 0.05, SESSIONS_PER_SEMESTER))
    return daily_attendance.astype(int)


def extract_features(attendance_record, window=EARLY_WINDOW):
    """
    Turns the first `window` sessions of a student's record into
    features the model can learn from.
    """
    early = attendance_record[:window]
    early_percentage = early.mean() * 100

    first_half = early[:window // 2]
    second_half = early[window // 2:]
    trend = (second_half.mean() - first_half.mean()) * 100  # positive = improving, negative = declining

    return [early_percentage, trend]


def main():
    X = []
    y = []

    for _ in range(NUM_SYNTHETIC_STUDENTS):
        record = simulate_one_student()
        features = extract_features(record)

        final_percentage = record.mean() * 100
        at_risk = 1 if final_percentage < 75 else 0

        X.append(features)
        y.append(at_risk)

    X = np.array(X)
    y = np.array(y)

    model = LogisticRegression()
    model.fit(X, y)

    train_accuracy = model.score(X, y)
    print(f"Trained on {NUM_SYNTHETIC_STUDENTS} synthetic students.")
    print(f"Training accuracy: {train_accuracy:.2%}")
    print(f"Feature weights -> [early_percentage, trend]: {model.coef_}")

    joblib.dump(model, 'risk_model.pkl')
    print("Saved model to risk_model.pkl")


if __name__ == '__main__':
    main()
