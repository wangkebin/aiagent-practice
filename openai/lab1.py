from dotenv import load_dotenv
from agents import Agent, Runner, trace
import asyncio
from pprint import pprint

load_dotenv(override=True)
agent = Agent(
    name="KebinLab1",
    instructions="You are a joke teller.",
    model="gpt-4o-mini"
)

def test():
    with trace("Tell me a joke."):
        result = asyncio.run(Runner.run(agent,"Tell me a daddy joke."))
        pprint(result.final_output)

def main():
    test()

if __name__ == "__main__":
    main()