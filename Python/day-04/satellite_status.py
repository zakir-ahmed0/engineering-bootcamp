def satellite_status(signal_strength):
    if signal_strength >= 80:
        return "Excellent"
    elif signal_strength >= 50:
        return "Good"
    else:
        return "Weak"

strength = satellite_status(100)
print(strength)
