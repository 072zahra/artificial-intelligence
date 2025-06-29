class MedicalExpertSystem:
    def __init__(self):
        self.conditions = {
            "flu": {"fever", "cough", "headache", "fatigue"},
            "cold": {"cough", "sneezing", "runny nose"},
            "migraine": {"headache", "nausea", "sensitivity to light"},
            "strep throat": {"fever", "sore throat", "swollen lymph nodes"},
        }

    def diagnose(self, symptoms):
        possible_conditions = []
        for condition, condition_symptoms in self.conditions.items():
            if symptoms.issubset(condition_symptoms):
                possible_conditions.append(condition)
        if possible_conditions:
            return f"Possible diagnosis: {', '.join(possible_conditions)}"
        else:
            return "No exact match found. Consider consulting a healthcare provider."

if __name__ == "__main__":
    medical_expert_system = MedicalExpertSystem()
    user_input = input("Enter your symptoms separated by commas: ").strip()
    user_symptoms = set(symptom.strip().lower() for symptom in user_input.split(","))
    diagnosis = medical_expert_system.diagnose(user_symptoms)
    print(diagnosis)
