class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_course = {}
        num_pre = [0]*numCourses
        for cur, pre in prerequisites:
            if pre not in pre_course:
                pre_course[pre] = [cur]    
            else:
                pre_course[pre] += [cur]
            num_pre[cur]+=1

        studied = []        # queue
        for ii in range(numCourses):
            if num_pre[ii]==0:
                studied.append(ii)
        if not studied: return False

        while studied:
            course_idx = studied.pop(0)

            if course_idx in pre_course:
                for idx in pre_course[course_idx]:
                    num_pre[idx] -= 1
                    if num_pre[idx]==0:
                        studied.append(idx)
        if max(num_pre)==0:
            return True
        return False