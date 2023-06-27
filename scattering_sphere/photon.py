import numpy as np

# Define photon class.
class Photon():
    def __init__(self, OPACITY):
        '''
        Initialises the photon at the centre of the sphere. 
        '''
        self.x = 0 # position
        self.y = 0
        self.z = 0
        self.dir_x = 0  # direction of travel
        self.dir_y = 0
        self.dir_z = 0
        
        # Initial scattering of the photon
        self.scatter()
        self.travel(OPACITY)

    def radiusCalc(self):
        '''
        Calculates the radius of the photon from the centre of the sphere
        '''
        r = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        return r

    def scatter(self):
        '''
        Scattering angle - Alters direction of travel
        '''
        phi = np.random.random()*np.pi
        theta = np.random.random()*2*np.pi
        self.dir_x = np.sin(phi)*np.cos(theta)
        self.dir_y = np.sin(phi)*np.sin(theta)
        self.dir_z = np.cos(phi)
        assert np.isclose(self.dir_x**2 + self.dir_y**2 + self.dir_z**2, 1) # Check direction is a unit vector.

    def travel(self, OPACITY):
        '''
        Travel distance - Alters position of photon
        '''
        eta = np.random.random() # I / I_0
        d = -np.log(eta)/OPACITY
        self.x += d*self.dir_x
        self.y += d*self.dir_y
        self.z += d*self.dir_z