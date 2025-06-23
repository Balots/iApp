from subprocess import run
import re
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='processing_logs.log', level=logging.INFO)

class ParseOrder:
    @staticmethod
    def name(i, log):
        text = log[i]
        pattern = r"Username: ([^\\]+)\\(.+)"
        match = re.search(pattern, text)
        return match.group(2)

    @staticmethod
    def ipv4(i, log):
        text = log[i]
        pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
        match = re.search(pattern, text)
        return match.group()

    @staticmethod
    def system(i, log):
        text = log[i]
        pattern = r"Windows\s+([\w\.]+\s*[\w]*)(?:\s+(Pro|Home|Enterprise|Education|SE|IoT))?"
        match = re.search(pattern, text)
        return match.group()

    @staticmethod
    def sysinfo(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def cpu(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def ram(i, log):
        res = []
        i += 1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line != '': res.append(line)
            i+=1
        return res

    @staticmethod
    def gpu(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def hdd(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def motherboard(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def adapter(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def battery(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def bios(i, log):
        res = []
        i+=1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line!='': res.append(line)
            i+=1
        return res

    @staticmethod
    def app(i, log):
        res = []
        pattern = r"\\Uninstall\\([^\\]+)$"
        i+= 1
        while log[i][0] != '[':
            line = log[i].replace('\x00', '').replace('=', '').replace('\n', '').replace(' ', '')
            if line == '': i+=1; continue
            if line == 'BREAK': break
            match = re.search(pattern, line)
            program = match.group(1)
            if program[0] == '{':
                tmp = run(['.\GUID.bat'], input=program, capture_output=True, text=True)
                program = tmp.stdout
            if line!='': res.append(program)
            i+=1
        return res


__FILE__ = f'PC_Hardware_Scan'
__ORDER__ = {'Username': ParseOrder.name,
             'Local IPv4': ParseOrder.ipv4,
             'SysVersion': ParseOrder.system,
             'System Information': ParseOrder.sysinfo,
             'Processor (CPU)': ParseOrder.cpu,
             'Memory (RAM)': ParseOrder.ram,
             'Graphics Card (GPU)': ParseOrder.gpu,
             'Storage Devices (HDD/SSD/NVMe)': ParseOrder.hdd,
             'Motherboard': ParseOrder.motherboard,
             'Network Adapters': ParseOrder.adapter,
             'Battery (if present)': ParseOrder.battery,
             'BIOS Information': ParseOrder.bios,
             'Programs (32-bit)': ParseOrder.app,
             'Programs (64-bit)': ParseOrder.app}

__SysReport__ = {

}

def script():
    name = 'PC_Hardware_Scan.log'
    if not name.startswith(__FILE__):
        logger.info('Error. Bad file formation!')
        exit()
    data = open(name, 'r', errors='ignore', encoding='utf-8').readlines()
    for item, order in __ORDER__.items():
        for i in range(len(data)):
            if item in data[i]:
                logger.info(f'{order} with item {item} has started.')
                __SysReport__[item] = order(i, data)
                logger.info(f'{__SysReport__[item]} has captured as {item}')

    return __SysReport__

if __name__ == "__main__":
    script()



