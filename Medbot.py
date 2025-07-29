welcome_prompt =("Welcome, Doctor. What would you like to do today\n"
                  "- To list all patients, press 1\n"
                  "-To run a new diagnosis, press 2\n"
                  "To quit, press q\n")

name_prompt = "What is the patients name?\n"

appearance_prompt = ("How is the patients general appearance?\n"
                      "1 Normal\n"
                      "2 Lethargic or irritable\n")

eye_prompt = "How are the patients eyes?\n - 1 Eyes normal or slightly sunken\n - 2 Eyes very sunken\n"

skin_prompt = ("How is the patients skin?\n"
               "- 1 Normal skin pinch\n"
               "-2 Slow skin pinch\n")

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

patients_and_diagnoses = [
  "Mike - Severe Dehydration",
  "Sally - Some Dehydration",
  "Kate - No dehydration",
]

error_message = "Sorry, please give patients name"




def save_new_diagnosis(name, diagnosis):
  if name == "" or diagnosis == "":
    print(error_message)
    return
  final_diagnosis = name + "-" + diagnosis
  patients_and_diagnoses.append(final_diagnosis)
  print("Final_diagnosis: " + final_diagnosis,"\n")
def main():
  while (True):
    selection = input(welcome_prompt)
    if selection == "1":
      list_patients()
    elif selection == "2":
      start_new_diagnosis()
    elif selection == "q":
      return

def list_patients():
  for patient in patients_and_diagnoses:
    print(patient)

def start_new_diagnosis():
  name = input(name_prompt)
  diagnosis = assess_appearance()
  save_new_diagnosis(name,diagnosis)

def assess_appearance():
  appearance = input(appearance_prompt)
  if appearance == "1":
    eyes = input(eye_prompt)
    return assess_eyes(eyes)
  elif appearance == "2":
    skin = input(skin_prompt)
    return assess_skin(skin)
  else:
    return""

def assess_eyes(eyes):
  if eyes == "1":
    return no_dehydration
  elif eyes == "2":
    return severe_dehydration
  else:
    return""

def assess_skin(skin):
  if skin == "1":
    return some_dehydration
  elif skin == "2":
    return severe_dehydration
  else:
    return ""



main()
