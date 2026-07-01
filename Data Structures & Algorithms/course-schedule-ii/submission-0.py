class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0]* numCourses

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course]+=1

        queue=[]
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        result =[]
        while queue:
            current = queue.pop(0)
            result.append(current)
            for next_course in adj_list[current]:
                in_degree[next_course]-=1
                if in_degree[next_course]==0:
                    queue.append(next_course)

        return result if len(result)== numCourses else []