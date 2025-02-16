from visualise import visualise
from particle import Particle
from particle_simulator import ParticleSimulator

def test_visualise():
    particles: list[Particle] = [Particle(0.3, 0.5, 1),
                 Particle(0.0, -0.5, -1),
                 Particle(-0.1, -0.4, 3)]
    
    simulator = ParticleSimulator(particles)
    visualise(simulator)

if __name__ == '__main__':
    test_visualise()