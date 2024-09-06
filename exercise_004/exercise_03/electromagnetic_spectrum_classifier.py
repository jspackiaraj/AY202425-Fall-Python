# Electromagnetic Spectrum Classifier
spectrum = {
    (10**-1, 10**3): "Radio waves",
    (10**-3, 10**-1): "Microwaves",
    (700, 10**-3): "Infrared",
    (400, 700): "Visible light",
    (10**-8, 400): "Ultraviolet",
    (10**-10, 10**-8): "X-rays",
    (10**-12, 10**-10): "Gamma rays"
}

wavelength = float(input("Enter the wavelength (in nm): "))
for (lower, upper), category in spectrum.items():
    if lower <= wavelength <= upper:
        print("This wavelength is in the", category, "category.")
        break
