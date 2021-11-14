import requests
import random
import string
import time
import os
import psutil

import matplotlib.pyplot as plt
import numpy as np

samples = 1000
ownerAddRuntimes = []
ownerAddCPU = []
ownerAddRAM = []
ownerModifyRuntimes = []
ownerModifyCPU = []
ownerModifyRAM = []

petAddRuntimes = []
petAddCPU = []
petAddRAM = []
petModifyRuntimes = []
petModifyCPU = []
petModifyRAM = []

fig, axs = plt.subplots(3)
fig1, axs1 = plt.subplots(3)
fig2, axs2 = plt.subplots(3)
fig3, axs3 = plt.subplots(3)

# Program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

print("")

# Owner Non-Functional Testing:
print("Owner Non-Functional Testing")
for item in range(samples):
    # Add operation through POST request.
    url = "http://localhost:8080/owners/new?"
    url += ("firstName=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("lastName=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("address=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("city=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("telephone=" + ( ''.join(random.choice(string.digits) for i in range(10)) ))
    payload={}
    headers = {}
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    end = time.time()
    ownerAddRuntimes.append(end - start)
    ownerAddCPU.append(psutil.cpu_percent())
    ownerAddRAM.append(psutil.virtual_memory().free / (1024 * 1000))

    # Modify operation through POST request.
    ownerId = item + 1
    url = "http://localhost:8080/owners/"
    url += (str(ownerId) + "/edit?")
    url += ("firstName=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("lastName=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("address=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("city=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("telephone=" + ( ''.join(random.choice(string.digits) for i in range(10)) ))
    payload={}
    headers = {}
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    end = time.time()
    ownerModifyRuntimes.append(end - start)
    ownerModifyCPU.append(psutil.cpu_percent())
    ownerModifyRAM.append(psutil.virtual_memory().free / (1024 * 1000))

    if ((item + 1) % 100 == 0):
        percentage = (100 * ((item + 1) / 1000))
        print(str(percentage) + "% Non-Functional Owner Add and Modify Operations Completed.")

print("Owner Non-Functional Testing Complete")

print("")

# Pet Non-Functional Testing:
print("Pet Non-Functional Testing")
for item in range(1, samples + 1, 1):
    # Add operation through POST request.
    ownerId = item
    url = "http://localhost:8080/owners/"
    url += (str(ownerId) + "/pets/new?")
    url += "id=&"
    url += ("name=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("birthDate=2006-06-06&")
    url += ("type=cat")
    payload={}
    headers = {}
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    end = time.time()
    petAddRuntimes.append(end - start)
    petAddCPU.append(psutil.cpu_percent())
    petAddRAM.append(psutil.virtual_memory().free / (1024 * 1000))

    # Modify operation through POST request.
    petId = item
    url = "http://localhost:8080/owners/"
    url += (str(ownerId) + "/pets/" + str(petId) + "/edit?")
    url += ("name=" + ( ''.join(random.choice(string.ascii_letters) for i in range(5)) ) + "&")
    url += ("birthDate=2007-07-07&")
    url += ("type=dog")
    payload={}
    headers = {}
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    end = time.time()
    petModifyRuntimes.append(end - start)
    petModifyCPU.append(psutil.cpu_percent())
    petModifyRAM.append(psutil.virtual_memory().free / (1024 * 1000))

    if (item % 100 == 0):
        percentage = (100 * (item / 1000))
        print(str(percentage) + "% Non-Functional Pet Add and Modify Operations Completed.")

print("Pet Non-Functional Testing Complete")

print("")
print("Generating Plots")

# Owner Add Operation Graphs
# Graph #1: Add Operation Runtime over Number of Owner Instances 
xpoints = np.array(range(samples))
ypoints = np.array(ownerAddRuntimes)
axs[0].plot(xpoints, ypoints)
axs[0].set_title("Graph #1: Add Operation Runtime over Number of Owner Instances")
axs[0].set(ylabel='Runtime (in s)')

# Graph #2: CPU Usage Percentage over Number of Owner Instances for Add Operation
xpoints = np.array(range(samples))
ypoints = np.array(ownerAddCPU)
axs[1].plot(xpoints, ypoints)
axs[1].set_title("Graph #2: CPU Usage Percentage over Number of Owner Instances for Add Operation")
axs[1].set(ylabel='CPU Usage (in %)')

# Graph #3: Available Free Memory over Number of Owner Instances for Add Operation
xpoints = np.array(range(samples))
ypoints = np.array(ownerAddRAM)
axs[2].plot(xpoints, ypoints)
axs[2].set_title("Graph #3: Free Memory Available over Number of Owner Instances for Add Operation")
axs[2].set(xlabel='Number of Owner Instances', ylabel='Available Free Memory (in MB)')

# Owner Modify Operation Graphs
# Graph #4: Modify Operation Runtime over Number of Owner Instances
xpoints = np.array(range(samples))
ypoints = np.array(ownerModifyRuntimes)
axs1[0].plot(xpoints, ypoints)
axs1[0].set_title("Graph #4: Modify Operation Runtime over Number of Owner Instances")
axs1[0].set(ylabel='Runtime (in s)')

# Graph #5: CPU Usage Percentage over Number of Owner Instances for Modify Operation
xpoints = np.array(range(samples))
ypoints = np.array(ownerModifyCPU)
axs1[1].plot(xpoints, ypoints)
axs1[1].set_title("Graph #5: CPU Usage Percentage over Number of Owner Instances for Modify Operation")
axs1[1].set(ylabel='CPU Usage (in %)')

# Graph #6: Available Free Memory over Number of Owner Instances for Modify Operation
xpoints = np.array(range(samples))
ypoints = np.array(ownerModifyRAM)
axs1[2].plot(xpoints, ypoints)
axs1[2].set_title("Graph #6: Free Memory Available over Number of Owner Instances for Modify Operation")
axs1[2].set(xlabel='Number of Owner Instances', ylabel='Available Free Memory (in MB)')

# Pet Add Operation Graphs
# Graph #7: Add Operation Runtime over Number of Pet Instances 
xpoints = np.array(range(samples))
ypoints = np.array(petAddRuntimes)
axs2[0].plot(xpoints, ypoints)
axs2[0].set_title("Graph #7: Add Operation Runtime over Number of Pet Instances")
axs2[0].set(ylabel='Runtime (in s)')

# Graph #8: CPU Usage Percentage over Number of Pet Instances for Add Operation
xpoints = np.array(range(samples))
ypoints = np.array(petAddCPU)
axs2[1].plot(xpoints, ypoints)
axs2[1].set_title("Graph #8: CPU Usage Percentage over Number of Pet Instances for Add Operation")
axs2[1].set(ylabel='CPU Usage (in %)')

# Graph #9: Available Free Memory over Number of Pet Instances for Add Operation
xpoints = np.array(range(samples))
ypoints = np.array(petAddRAM)
axs2[2].plot(xpoints, ypoints)
axs2[2].set_title("Graph #9: Free Memory Available over Number of Pet Instances for Add Operation")
axs2[2].set(xlabel='Number of Pet Instances', ylabel='Available Free Memory (in MB)')

# Pet Modify Operation Graphs
# Graph #10: Modify Operation Runtime over Number of Pet Instances
xpoints = np.array(range(samples))
ypoints = np.array(petModifyRuntimes)
axs3[0].plot(xpoints, ypoints)
axs3[0].set_title("Graph #10: Modify Operation Runtime over Number of Pet Instances")
axs3[0].set(ylabel='Runtime (in s)')

# Graph #11: CPU Usage Percentage over Number of Pet Instances for Modify Operation
xpoints = np.array(range(samples))
ypoints = np.array(petModifyCPU)
axs3[1].plot(xpoints, ypoints)
axs3[1].set_title("Graph #11: CPU Usage Percentage over Number of Pet Instances for Modify Operation")
axs3[1].set(ylabel='CPU Usage (in %)')

# Graph #12: Available Free Memory over Number of Pet Instances for Modify Operation
xpoints = np.array(range(samples))
ypoints = np.array(petModifyRAM)
axs3[2].plot(xpoints, ypoints)
axs3[2].set_title("Graph #12: Free Memory Available over Number of Pet Instances for Modify Operation")
axs3[2].set(xlabel='Number of Pet Instances', ylabel='Available Free Memory (in MB)')
  
print("")

# Owner Add Operation Averages
print("Owner Data Averages:")
averageOwnerRuntimeAdd = Average(ownerAddRuntimes)
averageOwnerCPUUsageAdd = Average(ownerAddCPU)
averageOwnerRAMUsageAdd = Average(ownerAddRAM)
print("Average Runtime per Add POST request to Owner:\t\t" + str(round(averageOwnerRuntimeAdd, 3)) + " seconds.")
print("Average CPU Usage per Add POST request to Owner:\t" + str(round(averageOwnerCPUUsageAdd, 3)) + "%.")
print("Average Free Memory per Add POST request to Owner:\t" + str(round(averageOwnerRAMUsageAdd, 3)) + " MB.")

# Owner Modify Operation Averages
averageOwnerRuntimeModify = Average(ownerModifyRuntimes)
averageOwnerCPUUsageModify = Average(ownerModifyCPU)
averageOwnerRAMUsageModify = Average(ownerModifyRAM)
print("Average Runtime per Modify POST request to Owner:\t" + str(round(averageOwnerRuntimeModify, 3)) + " seconds.")
print("Average CPU Usage per Modify POST request to Owner:\t" + str(round(averageOwnerCPUUsageModify, 3)) + "%.")
print("Average Free Memory per Modify POST request to Owner:\t" + str(round(averageOwnerRAMUsageModify, 3)) + " MB.")

print("")

# Pet Add Operation Averages
print("Pet Data Averages:")
averagePetRuntimeAdd = Average(petAddRuntimes)
averagePetCPUUsageAdd = Average(petAddCPU)
averagePetRAMUsageAdd = Average(petAddRAM)
print("Average Runtime per Add POST request to Pet:\t\t" + str(round(averagePetRuntimeAdd, 3)) + " seconds.")
print("Average CPU Usage per Add POST request to Pet:\t\t" + str(round(averagePetCPUUsageAdd, 3)) + "%.")
print("Average Free Memory per Add POST request to Pet:\t" + str(round(averagePetRAMUsageAdd, 3)) + " MB.")

# Pet Modify Operation Averages
averagePetRuntimeModify = Average(petModifyRuntimes)
averagePetCPUUsageModify = Average(petModifyCPU)
averagePetRAMUsageModify = Average(petModifyRAM)
print("Average Runtime per Modify POST request to Pet:\t\t" + str(round(averagePetRuntimeModify, 3)) + " seconds.")
print("Average CPU Usage per Modify POST request to Pet:\t" + str(round(averagePetCPUUsageModify, 3)) + "%.")
print("Average Free Memory per Modify POST request to Pet:\t" + str(round(averagePetRAMUsageModify, 3)) + " MB.")

plt.show()