
from typing import Optional
from typing import List
import heapq


class Solution:
    #https://leetcode.com/problems/course-schedule-iii/
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        c2 = []
        for c in courses:
            c2.append((c[1], c[0]))
        c2.sort()    
        t = 0
        res = 0
        a = []
        heapq.heapify(a)
        for c in c2:
            if t + c[1] <= c[0]:
                t += c[1]
                res += 1
                heapq.heappush(a, -c[1])
                continue
            
            if len(a) > 0:
                tmp = -heapq.heappop(a)
                if tmp > c[1]:
                    t = t - tmp + c[1]
                    heapq.heappush(a, -c[1])
                else:
                    heapq.heappush(a, -tmp) #возвращаем обратно
        
        return res








    #https://leetcode.com/problems/kth-largest-element-in-an-array/
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums)
        k = n + 1 - k
        res = 0
        for _ in range(k):
            res = heapq.heappop(nums)
        return res    

    # https://leetcode.com/problems/furthest-building-you-can-reach/
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        res = 0
        a = []
        heapq.heapify(a)
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                d = heights[i-1] - heights[i]
                if bricks + d >= 0:
                    bricks = bricks + d
                    heapq.heappush(a, d)
                    res = i
                else:
                    if ladders == 0:
                        #ничего сделать нельзя
                        break

                    res = i
                    ladders -= 1
                    t = 0
                    if (len(a) > 0):
                        t = heapq.heappop(a)
                    if (t > d):
                        if (t != 0):
                            #возвращаем t обратно
                            heapq.heappush(a, t)
                    else:
                        bricks = bricks - t
                        bricks = bricks + d
                        heapq.heappush(a, d)
            else:
                #движемся дальше
                res = i        

        return res

'''
heights = [253710,459585,71981,223232,977918,148680,123527,250812,260416,554767,473621,88538,966794,644116,865416,590993,550004,374573,105036,568303,460987,24602,757598,519047,263800,315868,963895,266638,598245,713310,489802,364169,742274,973483,807739,253747,564636,472387,598445,675408,626061,527760,922748,244691,41163,108095,953208,54400,191957,182321,801110,526756,11220,560896,782344,565351,570890,931781,511665,108738,357367,853555,674526,388790,686349,554731,102668,335287,461231,496065,489980,525209,693696,140598,784402,564477,743153,156379,370768,94810,121932,338323,972441,553422,865236,627884,673412,16147,858309,802780,150410,657225,761430,916149,644587,364929,661236,207648,507409,209803,663553,296241,51843,758342,448408,310536,733500,390516,580506,313748,729366,961156,766804,752158,713426,946971,433800,611365,806559,950149,831368,871881,132092,644626,150762,487527,365094,316637,684249,740162,605893,272845,416251,905202,984909,602362,424697,686193,566240,159584,600277,767037,211677,441897,586509,965864,393340,497044,881539,145921,159055,866123,603476,657682,284714,85306,470415,534245,641462,472616,159434,421500,843442,634366,625668,444943,657933,129173,914540,215272,598415,457087,437568,490742,172811,212016,435680,599042,789308,279873,689943,369130,618428,524390,877649,118759,60586,37618,20797,492854,946585,583767,944693,62988,358292,708659,23496,966718,557539,131703,358231,215464,771609,375770,855917,147866,543477,786910,760512,468183,542081,373398,979543,126508,361409,842847,872593,746682,893518,457222,978730,161753,697245,205997,363180,807952,795175,808090,462585,658667,186220,858457,923762,700792,294201,584816,514737,261038,327627,205592,221896,444108,979369,129394,44001,790354,353917,72772,330118,360651,635275,849492,966042,843108,158554,406317,995111,147752,121006,486157,678653,217657,4288,573547,820817,164534,921608,308037,373838,385901,343399,813472,58859,346176,68090,539503,322652,958331,832724,585003,75794,228299,31211,302603,601041,362034,300803,347024,650585,172193,876895,603734,165956,796982,786231,738823,562729,158032,364908,988395,775023,671485,424571,572157,623273,772919,914302,661979,920229,614760,934156,511607,889533,382154,82654,973121,549095,639792,412821,305216,74071,571794,969979,932469,335153,898442,938912,729489,872970,874332,8390,345366,901364,245104,315592,895028,533836,427909,737421,161915,510434,768573,179267,237370,562023,650593,869876,544314,464374,701215,789191,746271,871247,385836,788092,890101,286938,367130,635751,295576,607054,913206,556383,512305,253121,461980,951444,192012,897432,140517,842228,924286,268918,765459,344159,347853,592899,247814,379693,421908,295638,672994,774285,78096,886320,998456,10915,581642,549650,905526,186991,586693,320053,829130,465779,191060,238711,415584,273709,35854,55818,305798,667280,334370,121051,665390,230729,51662,904228,971349,7088,567705,265941,380847,760602,280222,351148,518112,609328,381795,46766,301829,886537,338310,130937,813816,446885,126867,578861,996302,56516,316900,648733,457604,903338,974707,336231,878687,776626,583241,353383,591761,438716,892530,231901,959454,915103,50735,453313,519651,940657,68380,38339,339705,19207,844122,483005,582959,592635,870233,208322,862826,598864,989646,583679,219396,371194,111781,493739,313465,383867,545219,171577,761747,992356,973874,497603,976481,136374,138311,918066,787696,929197,589326,801358,944697,28038,211029,752621,210197,491050,939207,254024,145811,767376,922553,796100,15858,899164,950319,728378,563113,532136,705190,290216,359946,214594,327241,641000,385347,786200,700340,576438,227606,498337,451637,425192,286305,472053,335562,587556,683468,290205,997253,868480,320419,392391,128015,674737,410783,136490,46713,154232,574917,904387,99900,490640,268209,994867,135705,390652,412028,404195,490553,184029,624391,836288,619242,570500,367786,908994,934572,226481,281181,469810,376226,354931,55711,43299,487568,853741,556475,842100,133451,371270,820314,735709,859169,992745,981261,506744,573542,544798,335063,71332,345306,551165,522500,148531,323820,525891,571989,109699,540927,391815,383139,528328,941384,577084,148432,537377,589708,613443,589827,688798,501198,304829,719726,181892,891384,237429,447803,49953,555945,69576,765896,194628,866362,533750,798399,369884,258270,964160,796047,420697,486470,781692,825420,689886,392317,278581,151823,184594,295461,723312,604322,248126,43623,91154,600821,55136,709242,990838,263827,564093,735641,174057,932157,750399,807534,338221,830644,171022,156968,351523,814982,403402,975555,955973,400091,523040,382185,577810,257717,544345,243199,509472,450948,839442,387377,553239,145202,822954,478559,487143,514465,587609,575770,547307,386320,410846,81519,599793,874316,730403,913822,800625,96868,913119,843783,699,767204,432828,496436,348230,767865,455134,266270,324004,863226,758456,66451,431182,641607,514915,522399,164590,335706,829719,724524,981933,812770,192582,880771,71867,704720,691726,761694,868674,964177,287148,124076,155241,535262,856554,108951,453851,597675,592745,32413,774791,750298,66826,876820,567338,699491,336474,60148,776819,430070,546456,564666,776689,886534,68830,749993,157504,933346,39836,417088,481438,30183,515310,764031,876787,321614,765291,466180,941767,877507,658149,60699,413225,849839,376668,689777,491763,712459,5768,608757,161358,554199,132368,464770,89566,309794,430979,979239,62376,354441,582188,947427,569030,430121,826059,562654,461350,901008,191328,484599,615686,859104,366550,140695,229053,282037,289028,296120,883539,980557,365526,143257,658629,730361,683520,101817,442395,50455,199765,137552,653983,47041,102020,308470,523274,447051,345263,967056,525031,506873,170405,995568,977216,83193,279492,376521,946443,847471,845107,321145,866307,523882,135730,824806,927733,605908,580895,177233,443804,914175,905847,661407,483093,518439,789231,66585,447439,14824,861841,89137,913636,194682,166773,212398,259259,160638,435374,941416,140851,311224,54813,155003,595354,742575,668942,77310,96783,217826,211522,116834,391751,922905,730508,225636,265187,995541,329461,244649,951125,322487,140958,608238,511144,410963,335698,228967,487748,382037,261094,363854,557078,539851,519352,364988,444038,284404,730251,828294,608545,188095,466810,46659,673970,142329,93794,167913,30119,116528,592075,810599,14144,445947,51745,236481,878706,838520,310352,112640,612690,663852,546444,818881,868195,573845,390221,254379]
bricks = 33671263
ladders = 108
sol = Solution()
r = sol.furthestBuilding(heights, bricks, ladders)
print(r)
'''
#589
'''
nums = [3,2,3,1,2,4,5,5,6] 
k = 4
sol = Solution()
r = sol.findKthLargest(nums, k)
print(r)
'''

sol = Solution()
courses = [[3,2],[4,3]]
r = sol.scheduleCourse(courses)
print(r)