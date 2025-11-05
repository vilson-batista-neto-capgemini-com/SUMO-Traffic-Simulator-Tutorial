import traci  # Static network information (such as reading and analyzing network files)

def get_reward(state): #2. Constraint 2
    """
    Simple reward function:
    Negative of total queue length to encourage shorter queues.
    """
    total_queue = sum(state[:-1])  # Exclude the current_phase element
    reward = -float(total_queue)
    return reward

def get_queue_length(detector_id): #8.Constraint 8
    return traci.lanearea.getLastStepVehicleNumber(detector_id)

def get_waiting_time(detector_id): #8.Constraint 8
    return traci.lane.getWaitingTime(detector_id)

def get_current_phase(tls_id): #8.Constraint 8
    return traci.trafficlight.getPhase(tls_id)

def set_start_traci(Sumo_config):
    traci.start(Sumo_config)

def set_gui_schema_traci(viewID, schemeName):
    traci.gui.setSchema(viewID, schemeName)

def set_simulation_step_traci():
    traci.simulationStep()

def set_traffic_light_phase_traci(tls_id, next_phase):
    traci.trafficlight.setPhase(tls_id, next_phase)

def get_all_traffic_light_program_logics(tls_id):
    return traci.trafficlight.getAllProgramLogics(tls_id)

def get_first_traffic_light_program_logics_by_ix(tls_id,index):
    return get_all_traffic_light_program_logics(tls_id)[index]

def get_first_traffic_light_program_logics(tls_id):
    return get_first_traffic_light_program_logics_by_ix(tls_id,0)

def set_close_traci():
    print("TraCI will close now")
    traci.close()
    print("TraCI is closed now")
