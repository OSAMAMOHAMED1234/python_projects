import time
def sleeper(seconds, i=-1):
	start_time = time.time()
	if i != -1:
		print(f'{i}\t{seconds}s')
	time.sleep(seconds)
	return time.time() - start_time

iteration_times = [1, 3, 2, 4]
run_time = 0
def main():
	global run_time
	for i, second in enumerate(iteration_times):
		run_time += sleeper(second, i=i)
main()
print(f'Ran for {run_time} seconds')

print("==================================================")

import asyncio
import time
iteration_times = [1, 3, 2, 4]
async def sleeper(seconds, i=-1):
	start_time = time.time()
	if i != -1:
		print(f'{i}\t{seconds}s')
	await asyncio.sleep(seconds)
	return time.time() - start_time

run_time = 0
total_compute_run_time = 0
async def main():
	global run_time
	global total_compute_run_time
	tasks = []
	for i, second in enumerate(iteration_times):
		tasks.append(
			asyncio.create_task(
				sleeper(second, i=i)
			)
		)
	results = await asyncio.gather(*tasks)
	for run_time_result in results:
		total_compute_run_time += run_time_result
		if run_time_result > run_time:
			run_time = run_time_result
asyncio.run(main())
print(f'Ran for {run_time} seconds, with a total of {total_compute_run_time} and {run_time / total_compute_run_time }')