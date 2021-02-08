def jobs_list_creator(line):
   return [int(x) for x in line.split(', ')]


def run_the_scheduling(jobs, index):
    searched_job_value = jobs[index]
    jobs = sorted(jobs)
    while True:
        job_to_remove_from_scheduling = jobs.pop()
        if job_to_remove_from_scheduling == searched_job_value:
            jobs.append(job_to_remove_from_scheduling)
            break
    return sum(jobs)


jobs_list = jobs_list_creator(input())
index = int(input())
print(run_the_scheduling(jobs_list, index))
