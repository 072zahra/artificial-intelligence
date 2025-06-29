class FamilyTreeExpertSystem:
    def __init__(self):
        self.knowledge_base = set()
    def add_relationship(self, person1, relation, person2):
        self.knowledge_base.add((person1, relation, person2))
        if relation == "parent":
            self.knowledge_base.add((person2, "child", person1))
        elif relation == "child":
            self.knowledge_base.add((person2, "parent", person1))
        elif relation == "sibling":
            self.knowledge_base.add((person2, "sibling", person1))
        elif relation == "spouse":
            self.knowledge_base.add((person2, "spouse", person1))
    def infer_relationship(self, person1, person2):
        for fact in self.knowledge_base:
            if fact[0] == person1 and fact[2] == person2:
                return fact[1]
        return "No direct relationship found."
family_expert_system = FamilyTreeExpertSystem()
per1 = input("Enter name of the first person : ")
per2 = input("Enter name of the second person : ")
re1 = input("Enter the relation : ").lower()
per3 = input("Enter name of the third person: ")
per4 = input("Enter name of the fourth person : ")
re2 = input("Enter the relation between person 2 and person 3 : ").lower()
re3 = input("Enter the relation between person 1 and person 4 : ").lower()
family_expert_system.add_relationship(per1, re1, per2)
family_expert_system.add_relationship(per1, re1, per3)
family_expert_system.add_relationship(per2, re2, per3)
family_expert_system.add_relationship(per1, re3, per4)
print(f"Relationship between {per1} and {per2}: {family_expert_system.infer_relationship(per1, per2)}")
print(f"Relationship between {per2} and {per3}: {family_expert_system.infer_relationship(per2, per3)}")
print(f"Relationship between {per1} and {per4}: {family_expert_system.infer_relationship(per1, per4)}")
print(f"Relationship between {per2} and {per4}: {family_expert_system.infer_relationship(per2, per4)}")