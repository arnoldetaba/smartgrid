import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import json
import pdb


IPS = []

def color_graph(val):
    if val < 45:
        return 'tab:green'
    if val >= 45 and val <=59:
        return 'tab:orange'
    if val >= 60:
        return 'tab:red'

def animate(i):
    graph_data = open("./GridControlUnit/log.txt").read()
    lines = graph_data.split('\n')
    ips_xy = {}
    # ips_xy = {
    #   "192.168.1.34": {
    #        "lamp1": {"xs":[.....], "ys":[....]},
    #        "lamp2": {"xs":[.....], "ys":[....]},
    #        "lamp3": {"xs":[.....], "ys":[....]},
    #   }
    #
    #   "192.168.1.52": {
    #        "lamp1": {"xs":[.....], "ys":[....]},
    #        "lamp2": {"xs":[.....], "ys":[....]},
    #        "lamp3": {"xs":[.....], "ys":[....]},
    #   }
    #
    #   "192.168.1.66": {
    #        "lamp1": {"xs":[.....], "ys":[....]},
    #        "lamp2": {"xs":[.....], "ys":[....]},
    #        "lamp3": {"xs":[.....], "ys":[....]},
    #   }
    #}
    xs = []
    x = 0
    for line in lines:
        if len(line) > 1:
            #pdb.set_trace()
            ip, data_json = line.split('=')
            ip = ip.strip()
            if ip not in ips_xy:
                IPS.append(ip)
                ips_xy[ip] = { 
                        "lamp1":{"xs":[], "ys":[]},
                        "lamp2":{"xs":[], "ys":[]},
                        "lamp3":{"xs":[], "ys":[]}
                        }
            data_json = data_json.strip()
            Y = json.loads(data_json.replace("'", '"'))
            #pdb.set_trace()
            ips_xy[ip]["lamp1"]["ys"].append(float(Y['lamp1']))
            ips_xy[ip]["lamp2"]["ys"].append(float(Y['lamp2']))
            ips_xy[ip]["lamp3"]["ys"].append(float(Y['lamp3']))
            #xs.append(x)
            ips_xy[ip]["lamp1"]["xs"].append(x)
            ips_xy[ip]["lamp2"]["xs"].append(x)
            ips_xy[ip]["lamp3"]["xs"].append(x)
            x += 1
            if len(ips_xy[ip]["lamp1"]["xs"]) >= 20:
                ips_xy[ip]["lamp1"]["ys"].pop(0)
                ips_xy[ip]["lamp2"]["ys"].pop(0)
                ips_xy[ip]["lamp3"]["ys"].pop(0)

                ips_xy[ip]["lamp1"]["xs"].pop(0)
                ips_xy[ip]["lamp2"]["xs"].pop(0)
                ips_xy[ip]["lamp3"]["xs"].pop(0)

    #pdb.set_trace()
    exit_loop = 0
    for ip in ips_xy:
        if exit_loop == 0:
            ax1.clear()
            ax1.title.set_text(f"{ip} : \nlamp1,lamp2,lamp3")
            val = max(ips_xy[ip]["lamp1"]["ys"])
            ax1.plot(ips_xy[ip]["lamp1"]["xs"], ips_xy[ip]["lamp1"]["ys"], color_graph(val))

            ax3.clear()
            #ax3.title.set_text(f"{ip} : lamp2")
            val = max(ips_xy[ip]["lamp2"]["ys"])
            ax3.plot(ips_xy[ip]["lamp2"]["xs"], ips_xy[ip]["lamp2"]["ys"], color_graph(val))

            ax5.clear()
            #ax5.title.set_text(f"{ip} : lamp3")
            val = max(ips_xy[ip]["lamp3"]["ys"])
            ax5.plot(ips_xy[ip]["lamp2"]["xs"], ips_xy[ip]["lamp3"]["ys"], color_graph(val))

            exit_loop += 1
        elif exit_loop == 1:
            ax2.clear()
            ax2.title.set_text(f"{ip} : lamp1, lamp2, lamp3")
            #pdb.set_trace()
            val = max(ips_xy[ip]["lamp1"]["ys"])
            #pdb.set_trace()
            ax2.plot(ips_xy[ip]["lamp1"]["xs"], ips_xy[ip]["lamp1"]["ys"], color_graph(val))

            ax4.clear()
            #ax4.title.set_text(f"{ip} : lamp2")
            val = max(ips_xy[ip]["lamp2"]["ys"])
            ax4.plot(ips_xy[ip]["lamp2"]["xs"], ips_xy[ip]["lamp2"]["ys"], color_graph(val))

            ax6.clear()
            #ax6.title.set_text(f"{ip} : lamp3")
            val = max(ips_xy[ip]["lamp3"]["ys"])
            ax6.plot(ips_xy[ip]["lamp3"]["xs"], ips_xy[ip]["lamp3"]["ys"], color_graph(val))
            exit_loop += 1
        else:
            break


style.use('fivethirtyeight')

fig = plt.figure()

# the big subplot, to carry labels
#ax = fig.add_subplot(1,1,1)
#ax.set_xlabel("temp (s)")
#ax.set_ylabel("Consommation (watts W)")

# lampice1
ax1 = fig.add_subplot(3, 2, 1)
ax1.set_ylim([0, 100])

ax3 = fig.add_subplot(3, 2, 3)
ax3.set_ylim([0, 100])

ax5 = fig.add_subplot(3, 2, 5)
ax5.set_ylim([0, 100])


# lampice2
ax2 = fig.add_subplot(3, 2, 2)
ax2.set_ylim([0, 100])

ax4 = fig.add_subplot(3, 2, 4)
ax4.set_ylim([0, 100])

ax6 = fig.add_subplot(3, 2, 6)
ax6.set_ylim([0, 100])


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
