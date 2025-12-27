from src.graph import app
import asyncio
async def run_test(text):
    print(f"\n--- Testing: '{text}' ---")
    inputs = {"original_text": text}
    result = await app.ainvoke(inputs)
    print(f"RESULT: {result}")

if __name__ == "__main__":
    # Test 1: Should Pass
    asyncio.run(run_test("hello world"))
    
    # Test 2: Should Fail (PII)
    asyncio.run(run_test("contact me at test@gmail.com"))