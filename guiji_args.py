#encoding: utf-8
#用来比较每次rosvio的不同之处
import argparse
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--tru_fname', type=str, default='00') 
parser.add_argument('--myres_fname', type=str, default='00')
args = parser.parse_args()

filename1 =args.tru_fname;
filename2 = args.myres_fname;






NS1 = np.loadtxt(filename1);
NS2 = np.loadtxt(filename2);




time1 = NS1[:,0];
#time0=
#time1 = (NS2[:,0]-NS2[0,0])*10**(-9);

fig = plt.figure(1);
ax = fig.add_subplot(111, projection='3d');
p11,=ax.plot(NS1[:,1],NS1[:,2],NS1[:,3]);#noros_ORBVIO
p12,=ax.plot(NS2[:,1],NS2[:,2],NS2[:,3]);#stereoORB
#p13,=ax.plot(NS1[:,0],NS1[:,1],NS1[:,2]);#groundtruin cam
#p14,=ax.plot(NS2[:,1],NS2[:,2],NS2[:,3]);#groundtruin ref (original)
#p15,=ax.plot(NS3[:,1],NS3[:,2],NS3[:,3]);#ros_ORBVIO (其实这个应该是在body即imu坐标系下的关键帧的轨迹)
#p16,=ax.plot(NS4[:,1],NS4[:,2],NS4[:,3]);
#p17,=ax.plot(NS5[:,1],NS5[:,2],NS5[:,3]);


#ax.legend([p11,p12,p13,p14,p15],["est","stereo","trumodi","tru","estros"] );
ax.legend([p11,p12],["groundtru","prioraid_res"] );
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('compare with the groundtru');
#plt.savefig(filepath+'guiji3.eps', format="eps");

# fig = plt.figure(2);
# ax0 = fig.add_subplot(111, projection='3d');
# p21,=ax0.plot(NS[:,1],NS[:,2],NS[:,3]);
# p12,=ax0.plot(NS0[:,3],NS0[:,7],NS0[:,11]);
# ax0.legend([p21],["est","stereo"] );
# ax0.set_xlabel('X')
# ax0.set_ylabel('Y')
# ax0.set_zlabel('Z')
# plt.title('esti Position in initial frame');
# plt.savefig(filepath+'guiji1.eps', format="eps");
#
#
plt.show();




#scale = np.loadtxt(filepath+'scale.txt');
#plt.figure(2);
#[p21,p22] = plt.plot(scale[:,0]-scale[0,0],scale[:,1:3]);
#plt.title('scale');
#plt.legend([p21,p22],['aftopt','befopt']);
#plt.savefig(filepath+'/scale.eps', format="eps")




#       f << setprecision(6) << pKF->mTimeStamp << setprecision(7) << " ";
#        f << P(0) << " " << P(1) << " " << P(2) << " ";
#       f << V(0) << " " << V(1) << " " << V(2) << " ";
#        f << q.x() << " " << q.y() << " " << q.z() << " " << q.w() << " ";
#        f << bg(0) << " " << bg(1) << " " << bg(2) << " ";
#        f << ba(0) << " " << ba(1) << " " << ba(2) << " ";
#       f << dbg(0) << " " << dbg(1) << " " << dbg(2) << " ";
#       f << dba(0) << " " << dba(1) << " " << dba(2) << " ";
#       f << endl;
