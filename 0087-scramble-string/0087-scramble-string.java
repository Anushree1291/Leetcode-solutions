class Solution {
    Map<String,Boolean> a=new HashMap<String,Boolean>();
    
    public boolean isScramble(String s1, String s2) {
        if (s1.length()!=s2.length()) return false;
        if (s1.equals(s2)) return true;
        return fun(s1,s2);
    }
    
    boolean fun(String s1,String s2){
        int n=s1.length();
        String k=s1+"#"+s2;
        
        //System.out.println(s1+" "+s2);
        
        if (s1.equals(s2)){
            a.put(k,true);
            return true;
        }
        else if (a.containsKey(k))  return a.get(k);
        else if(n==1) return false;
        
        for(int i=1;i<=n-1;i++){
            //System.out.println(b1+" "+b2+" "+b3+" "+b4);
            
            if((fun(s1.substring(0,i),s2.substring(0,i))) && (fun(s1.substring(i),s2.substring(i)))){
                a.put(k,true);
                return true;
            }
            if((fun(s1.substring(0,i),s2.substring(n-i))) && (fun(s1.substring(i),s2.substring(0,n-i)))){
                a.put(k,true);
                return true;
            }
            
        }
        a.put(k,false);
        return false;
    }
    
}