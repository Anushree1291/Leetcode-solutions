import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int maxSatisfaction(int[] sa) {
        Integer[] s=Arrays.stream(sa).boxed().toArray(Integer[] ::new);
        Arrays.sort(s, Collections.reverseOrder());
        if(s[0]<0){
            return 0;
        }
        int m=s[0];
        int p=s[0];
        for(int i=1;i<s.length;i++){
            p+=s[i];
            if(m+p<m){
                return m;
            }
            m+=p;
        }
        return m;
    }
}