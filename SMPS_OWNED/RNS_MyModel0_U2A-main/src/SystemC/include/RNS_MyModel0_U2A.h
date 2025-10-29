/***************************************************************************
 * Copyright 1996-2025 Synopsys, Inc.
 *
 * This Synopsys software and all associated documentation are proprietary
 * to Synopsys, Inc. and may only be used pursuant to the terms and
 * conditions of a written license agreement with Synopsys, Inc.
 * All other use, reproduction, modification, or distribution of the
 * Synopsys software or the associated documentation is strictly prohibited.
 ***************************************************************************/
 

/***************************************************************************
 * Generated snippet, used for detecting user edits.
 * CHECKSUM:f54ecae731529cb1040e1bb28fc6d5e08c855757
 ***************************************************************************/
 
#pragma once

#include "RNS_MyModel0_U2ABase.h"


/**
 * \copydoc RNS_MyModel0_U2ABase
 */
class RNS_MyModel0_U2A : public RNS_MyModel0_U2ABase {
  public:
#if (defined SYSTEMC_VERSION && SYSTEMC_VERSION <= 20221128 /*2.3.4*/)
    SC_HAS_PROCESS(RNS_MyModel0_U2A);
#endif

    RNS_MyModel0_U2A(sc_core::sc_module_name name);

  private:
    friend class RNS_MyModel0_U2ACovermodel;

    
    
  private:
        
};

