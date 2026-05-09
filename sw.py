from pyscript import document  # type: ignore

classmates = [
    "Akingson Jake G Ayake from Topaz and my favorite subject is Science",
    "Ashley Kirsten Y. Santos from Topaz and my favorite subject is Science",
    "John Vicent T Ligas from Topaz and my favorite subject is Math",
    "Alexander Tacan from Topaz and my favorite subject is English",
    "Giovanni D Escarda from Topaz and my favorite subject is Music",
]


def get_output():
    return document.getElementById("classmatefav")


def formatted_classmates():
    return "\n".join(classmates)


def add_classmate(event=None):
    output = get_output()
    output.innerText = "" if output.innerText else formatted_classmates()


def add_you(event=None):
    field_ids = ["classmateInput", "classmateInput1", "classmateInput2"]
    values = [document.getElementById(field).value.strip() for field in field_ids]

    if all(values):
        name, section, subject = values
        classmates.append(f"{name} from {section} and my favorite subject is {subject}")
        for field in field_ids:
            document.getElementById(field).value = ""
