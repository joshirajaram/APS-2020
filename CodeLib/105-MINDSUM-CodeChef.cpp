#include<bits/stdc++.h>
#define Loop(i,a,b) for(int i=a;i<b;++i)
#define NLoop(i,a,b) for(int i=a;i>=b;--i)
#define print(arr,n,m) for(int i=0;i<n;++i) { for(int j=0;j<m;++j) cout<<arr[i][j]<<" "; cout<<endl; }
#define print2(arr,n) for(int i=0;i<n;++i) { cout<<arr[i]<<" "; } cout<<endl;
#define mp(a,b) make_pair(a,b)
using namespace std;
typedef long long int ll;
ll SOD(ll n)
{
	ll s = 0;
	while(n!=0)
	{
		s+= n%10;
		n/=10;
	}
	return s;
}
ll ultiSOD(ll n, ll &op)
{
	while(n>=10) 
	{
		n = SOD(n);
		op++;
	}
	return n;
}
int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int t;
	cin>>t;
	while(t--)
	{
		ll n,d;
		cin>>n>>d;
		vector<ll> steps(10,-1);
		queue< pair<ll,ll> > q;
		q.push(mp(n,0));
		ll co = 0;
		ll start = ultiSOD(n,co);
		
		while(!q.empty())
		{
			ll a = q.front().first;
			ll b = q.front().second;
			//cout<<a<<" "<<b<<endl;
			q.pop();
			if(a<10 && steps[a]==-1) steps[a] = b;
			else if(a<10 && steps[a]!=-1 && a==start) break;
			else q.push(mp(SOD(a),b+1));
			q.push(mp(a+d,b+1));
		}
		for(ll i=1;i<10;++i) 
		{
			if(steps[i]!=-1) 
			{
				cout<<i<<" "<<steps[i]<<endl;
				break;
			}
		}
	}
}
