import matplotlib.pyplot as plt
measured_data = [10,23,45,50,100,155,204,255]
plt.plot(measured_data)
plt.show()

measured_data_str = [str(item) for item in measured_data]

with open("data.txt", "w") as outfile:
    outfile.write("/n".join(measured_data_str))
    
