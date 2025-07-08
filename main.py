from req import *
from asyncio import run
from json import dump

__DOMAIN_NAMES__ = [
"""
Your network computers might be write here.
"""]

def main():
    for name in __DOMAIN_NAMES__:
        collector = RequestCollector(name)

        try:run(collector.execute_gather())
        except Exception as e: print(f'WARNING: Error during process computer {name}. Program exit with message: {e}')

        result = collector.get_results()
        with open(f"results\\{name}.json", "w", encoding="utf-8") as f:
            dump(result, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()
