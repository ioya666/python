def evaluate_temperature(temperature):
    if (temperature <= 10):
        return "WAHH DET ER KOLDT MIG BLIV SENG"
    if (temperature <= 15):
        return "WAHH DET ER KOLDT MIG BLIV HJEMME NO ARBEJDE"
    if (temperature <= 20):
        return "AHH DET ER FANTASTISK VEJR MIG GÅ SKOV"
    if (temperature <= 22):
        
        return "picasso me like it"
    return "ME STRAND XD"

def promt_for_number(message):
    line = input(f"{message}")
    return float(line)

def confirm(question):
    affirmative = "ja"
    reject = "nej"
    while True:
        response = input(f"{question} ")
        if response in [affirmative, reject]:
            break
        print(f"nuh uh that ont work here boi, svar enten '{affirmative}' eller '{reject}'")
    return response == affirmative

def main():
    print("Temperatur tier list")
    while True:
        temperature = promt_for_number("what is temperaturen i grader celsius?")
        result = evaluate_temperature(temperature)
        print(result)

        if not confirm("tri agane?"):
            break

if __name__ == "__main__":
    main()
    