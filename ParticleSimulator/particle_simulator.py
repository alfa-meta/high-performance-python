from particle import Particle

class ParticleSimulator:
    def __init__(self, particle_list: list[Particle]):
        self.particle_list: list[Particle] = particle_list

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particle_list:
                # 1. Caclulate the direction
                norm = (p.x**2 + p.y**2) ** 0.5
                v_x = -p.y/norm
                v_y = p.x/norm


                # 2. Caclulate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y

                # 3. Repeat for all the time steps.

