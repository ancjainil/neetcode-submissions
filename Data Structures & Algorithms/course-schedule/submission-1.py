class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0]* numCourses
        def has_cycle(course):
            if visited[course]==1:
                return True

            if visited[course]==2:
                return False

            visited[course]=1

            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
                
            visited[course]=2
            return False


        for course in range(numCourses):
                if visited[course]==0:
                    if has_cycle(course):
                        return False

        return True